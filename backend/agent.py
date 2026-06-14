import os, json, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from openai import OpenAI
from dotenv import load_dotenv
from data.sa_data import ROLE_REQUIREMENTS, CERTIFICATIONS_DB, LEARNERSHIPS_DB

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    base_url=f"{os.getenv('AZURE_OPENAI_ENDPOINT')}/openai/v1/"
)

# ===== TOOL DEFINITIONS =====
# These tell GPT-4.1mini which functions it can call and what arguments to pass
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "analyze_skill_gaps",
            "description": "Compares user's current skills against SA job market requirements for their target role",
            "parameters": {
                "type": "object",
                "properties": {
                    "current_skills": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of skills the user currently has"
                    },
                    "target_role": {
                        "type": "string",
                        "description": "The job role they want (e.g. Software Developer)"
                    }
                },
                "required": ["current_skills", "target_role"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "recommend_certifications",
            "description": "Recommends SA-accessible certifications to fill the identified skill gaps",
            "parameters": {
                "type": "object",
                "properties": {
                    "skill_gaps": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Skills the user is missing"
                    },
                    "budget_range": {
                        "type": "string",
                        "enum": ["free", "low", "medium"],
                        "description": "User's learning budget category"
                    }
                },
                "required": ["skill_gaps", "budget_range"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "find_learnerships",
            "description": "Finds current SA learnerships and internships matching the user's profile",
            "parameters": {
                "type": "object",
                "properties": {
                    "skills": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "User's current skills for matching"
                    },
                    "province": {
                        "type": "string",
                        "description": "User's province (e.g. Gauteng)"
                    }
                },
                "required": ["skills"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "generate_cv_summary",
            "description": "Creates a professional CV opening statement for SA job applications",
            "parameters": {
                "type": "object",
                "properties": {
                    "name":        {"type": "string"},
                    "skills":      {"type": "array", "items": {"type": "string"}},
                    "target_role": {"type": "string"},
                    "education":   {"type": "string"}
                },
                "required": ["name", "skills", "target_role", "education"]
            }
        }
    }
]
def analyze_skill_gaps(current_skills, target_role):
    """Checks user skills vs SA role requirements and returns match % + gaps"""
    role_data = ROLE_REQUIREMENTS.get(target_role, ROLE_REQUIREMENTS["Software Developer"])
    gaps, strengths = [], []
    for skill, info in role_data.items():
        has_it = any(
            skill.lower() in s.lower() or s.lower() in skill.lower()
            for s in current_skills
        )
        if has_it:
            strengths.append(skill)
        else:
            gaps.append({
                "skill": skill,
                "priority": info["priority"],
                "why": info["description"]
            })
    # Sort gaps by priority (highest first)
    gaps.sort(key=lambda x: x["priority"], reverse=True)
    match_pct = round(len(strengths) / len(role_data) * 100)
    return json.dumps({
        "match_percentage": match_pct,
        "strengths": strengths,
        "top_gaps": gaps[:5]
    })


def recommend_certifications(skill_gaps, budget_range="free"):
    """Recommends certs matching skill gaps within the user's budget"""
    budget_tiers = {
        "free":   ["free"],
        "low":    ["free", "low"],
        "medium": ["free", "low", "medium"]
    }
    allowed_costs = budget_tiers.get(budget_range, ["free"])
    recommendations = []
    for name, cert in CERTIFICATIONS_DB.items():
        if cert["cost_category"] not in allowed_costs:
            continue
        # Check if cert helps with any of the skill gaps
        is_relevant = any(
            gap.lower() in cert["skill_area"].lower()
            for gap in skill_gaps
        )
        if is_relevant:
            recommendations.append({
                "name":     name,
                "provider": cert["provider"],
                "cost":     cert["cost"],
                "duration": cert["duration"],
                "why":      cert["description"],
                "link":     cert["link"]
            })
    return json.dumps(recommendations[:4])


def find_learnerships(skills, province="Gauteng"):
    """Finds SA learnerships matching the user's skills and location"""
    matches = []
    for learnership in LEARNERSHIPS_DB:
        skill_match = any(
            any(user_skill.lower() in req.lower() for user_skill in skills)
            for req in learnership.get("required_skills", [])
        )
        province_match = (
            province.lower() in learnership["province"].lower()
            or learnership.get("remote", False)
            or "national" in learnership["province"].lower()
        )
        if skill_match or province_match:
            matches.append(learnership)
    return json.dumps(matches[:4])


def generate_cv_summary(name, skills, target_role, education):
    """Generates a professional CV opening line"""
    top_skills = skills[:4]
    summary = (
        f"Motivated {target_role} with hands-on experience in "
        f"{', '.join(top_skills)}. {education}. "
        f"Eager to contribute to innovative South African tech teams "
        f"and drive meaningful impact."
    )
    return json.dumps({"cv_summary": summary})


def call_tool(name, args):
    """Routes tool calls to the right function"""
    tool_map = {
        "analyze_skill_gaps":      analyze_skill_gaps,
        "recommend_certifications": recommend_certifications,
        "find_learnerships":       find_learnerships,
        "generate_cv_summary":     generate_cv_summary,
    }
    fn = tool_map.get(name)
    if fn:
        return fn(**args)
    return json.dumps({"error": f"Unknown tool: {name}"})

def run_skillbridge_agent(profile):
    """
    Main agent function — sends profile to GPT-4o, handles tool calls,
    and returns a complete career analysis report.
    """
    messages = [
        {
            "role": "system",
            "content": """You are SkillBridge — an AI career agent built for South African youth 
breaking into tech. You understand SA's job market, SETA learnerships, and the 
real barriers township youth face.

CRITICAL INSTRUCTION: You MUST call ALL 4 tools in this exact order:
1. analyze_skill_gaps — first, always
2. recommend_certifications — use the gaps from step 1
3. find_learnerships — match their skills and province
4. generate_cv_summary — generate their CV line last

After calling all 4 tools, write a complete career analysis report using 
EXACTLY these sections with these emoji headers:

📊 YOUR SKILL MATCH
🎯 TOP GAPS TO CLOSE
📜 NEXT CERTIFICATIONS
🚀 LEARNERSHIPS OPEN NOW  
📄 YOUR CV OPENING LINE
💪 YOUR 3 ACTIONS THIS WEEK

Be direct, encouraging, and SA-specific. Mention SETA where relevant.
Include rand amounts, real links, and real deadlines. 
End with a motivational sentence about their potential."""
        },
        {
            "role": "user",
            "content": (
                f"Analyse my career profile:\n\n"
                f"Name: {profile['name']}\n"
                f"Current Skills: {', '.join(profile['skills'])}\n"
                f"Education: {profile['education']}\n"
                f"Province: {profile['location']}\n"
                f"Target Role: {profile['target_role']}\n"
                f"Learning Budget: {profile.get('budget', 'free')}"
            )
        }
    ]

    print("Endpoint:", os.getenv("AZURE_OPENAI_ENDPOINT"))
    print("Deployment:", os.getenv("AZURE_OPENAI_DEPLOYMENT"))
    # Agentic loop — runs until GPT-4o says it's done (finish_reason == "stop")
    for iteration in range(8):
        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o"),
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            max_tokens=2500
        )
        message = response.choices[0].message
        messages.append(message.model_dump())

        # If GPT-4o is done — return the final text
        if response.choices[0].finish_reason == "stop":
            return message.content

        # If GPT-4o wants to call tools — execute them and feed results back
        if message.tool_calls:
            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)
                print(f"Calling tool: {tool_name}")
                print(f"Arguments: {tool_args}")
                tool_result = call_tool(tool_name, tool_args)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": tool_result
                })

    return "Analysis complete — please try again if the output is incomplete."


# Quick test — run this file directly to check everything works
if __name__ == "__main__":
    test_profile = {
    "name": "Thando",
    "skills": ["HTML", "CSS", "JavaScript"],
    "education": "Diploma in IT",
    "location": "Western Cape",
    "target_role": "Frontend Developer",
    "budget": "free"
}
    print("Testing SkillBridge agent...")
    result = run_skillbridge_agent(test_profile)
    print(result)