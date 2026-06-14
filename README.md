# SkillriBdge-AI-agent
AI-powered reasoning agent that helps South African youth identify skill gaps, discover certifications, find learnerships, and generate career development plans.
# SkillBridge — AI Career Agent for South African Youth

## The Problem
Millions of young South Africans want to break into tech but don't know:
- Which skills to learn first for SA's actual job market
- Which certifications are achievable on their budget
- Which learnerships are currently accepting applications
- How to write a CV that gets interviews

## The Solution
SkillBridge is an AI agent that takes a user's profile and generates:
- **Skill gap analysis** vs the SA job market (match percentage + priorities)
- **Certification roadmap** with real ZAR costs and free options
- **Live learnerships** currently accepting applications in SA
- **Professional CV opening line** ready to paste

Note: Current learnership and certification information is sourced from curated South African opportunity datasets and can be extended with live integrations in future releases.

## Architecture
```
User Form → Flask API → Azure AI Foundry (GPT-4.1-mini)
                              ↓
              ┌───────────────────────────────────┐
              │ Tool 1: analyze_skill_gaps         │
              │ Tool 2: recommend_certifications   │  → sa_data.py
              │ Tool 3: find_learnerships          │
              │ Tool 4: generate_cv_summary        │
              └───────────────────────────────────┘
                              ↓
                     Synthesised Career Report
```

## Tech Stack
- **AI Reasoning**: Azure AI Foundry — GPT-4.1-mini with function calling
- **Backend**: Python 3.11 + Flask
- **Frontend**: HTML/CSS/JavaScript
- **AI Coding**: GitHub Copilot (required for Creative Apps track)

## Running Locally
```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/skillbridge.git
cd skillbridge

# 2. Create .env with your Azure keys (see .env.example)
# 3. Install dependencies
pip install -r backend/requirements.txt

# 4. Start the server
python backend/app.py

# 5. Open frontend/index.html in your browser
```

## Impact
Built for the ~9 million unemployed youth in South Africa.
Democratises career guidance previously available only to the privileged.

## Hackathon
Microsoft Agents League Hackathon 2026
Category: **Hack for Good**
Built by: [AARON KGAPHOLA] — Orange Farm, Gauteng, South Africa
