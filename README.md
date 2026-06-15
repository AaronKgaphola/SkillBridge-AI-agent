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

- This is the home page.
<img width="830" height="315" alt="Screenshot 2026-06-15 083927" src="https://github.com/user-attachments/assets/f799a996-09d7-45f7-97a1-f78462fdaa4e" />

- This is what it looks like before the user enters thier information.
<img width="1901" height="912" alt="Screenshot 2026-06-15 081053" src="https://github.com/user-attachments/assets/54e5792a-3339-4a9e-b657-b3638dadab87" />

- After the user enters the information it would look like this.
<img width="1896" height="906" alt="Screenshot 2026-06-15 081237" src="https://github.com/user-attachments/assets/b7df849e-f024-4f80-96be-91a3adfa9416" />

- The results are gerenerated after the user presses "Analyze my carrer path".
<img width="898" height="908" alt="Screenshot 2026-06-15 081330" src="https://github.com/user-attachments/assets/6418c1eb-7d60-4fce-b293-d8400a8b5d48" />

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
<img width="1021" height="741" alt="skillbridge-architecture" src="https://github.com/user-attachments/assets/0e720957-4cd4-409d-8dd5-6b24185540d8" />

## Tech Stack
- **AI Reasoning**: Azure AI Foundry — GPT-4.1-mini with function calling
- **Backend**: Python 3.11 + Flask
- **Frontend**: HTML/CSS/JavaScript
- **AI Coding**: GitHub Copilot (required for Creative Apps track)

<img width="1901" height="910" alt="Screenshot 2026-06-15 080947" src="https://github.com/user-attachments/assets/757db433-c1e9-4bf6-b132-da790f7444d7" />


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
<img width="911" height="912" alt="Screenshot 2026-06-15 081405" src="https://github.com/user-attachments/assets/6559571f-100d-4034-95b7-d9f52195ea25" />


## Hackathon
Microsoft Agents League Hackathon 2026
Category: **Hack for Good**
Built by: [AARON KGAPHOLA] — Orange Farm, Gauteng, South Africa
