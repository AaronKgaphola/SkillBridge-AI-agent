ROLE_REQUIREMENTS = {
    "Software Developer": {
        "Python":      {"priority": 5, "description": "Core language — every SA dev role needs this"},
        "JavaScript":  {"priority": 4, "description": "Web dev — React, Node, Angular all need this"},
        "Git":         {"priority": 5, "description": "Version control — no job exists without this"},
        "SQL":         {"priority": 4, "description": "Database querying — used everywhere in SA"},
        "REST APIs":   {"priority": 4, "description": "How systems talk — critical skill"},
        "Linux/Bash":  {"priority": 3, "description": "All servers run Linux"},
        "React":       {"priority": 3, "description": "Most popular SA frontend framework"},
        "Docker":      {"priority": 3, "description": "Containerisation — growing fast in SA"},
        "AWS/Azure":   {"priority": 3, "description": "Cloud — employers want this now"},
        "Agile/Scrum": {"priority": 3, "description": "How teams work in SA companies"},
    },
    "Cloud Engineer": {
        "AWS":         {"priority": 5, "description": "Amazon — dominant in SA enterprise"},
        "Azure":       {"priority": 5, "description": "Microsoft — big in SA government/banking"},
        "Linux":       {"priority": 5, "description": "All cloud runs on Linux"},
        "Networking":  {"priority": 4, "description": "TCP/IP, DNS, VPNs — cloud foundation"},
        "Python":      {"priority": 4, "description": "Automation and scripting"},
        "Terraform":   {"priority": 4, "description": "Infrastructure as code"},
        "Docker":      {"priority": 4, "description": "Containers — cloud standard"},
        "Security":    {"priority": 4, "description": "Cloud security — every SA bank needs this"},
        "CI/CD":       {"priority": 3, "description": "GitHub Actions, Jenkins"},
    },
    "Systems Developer": {
        "Python":          {"priority": 5, "description": "IQ Business, BCX, Investec all use this"},
        "Java":            {"priority": 4, "description": "SA banking — Standard Bank, FNB"},
        "SQL":             {"priority": 5, "description": "Every system touches a database"},
        "Git":             {"priority": 5, "description": "Non-negotiable in any team"},
        "REST APIs":       {"priority": 4, "description": "System integration — SA speciality"},
        "Testing":         {"priority": 4, "description": "Unit tests, integration tests"},
        "Design Patterns": {"priority": 3, "description": "MVC, SOLID — senior interviews"},
        "Linux":           {"priority": 3, "description": "Deployment environment"},
        "Agile":           {"priority": 4, "description": "SCRUM, Kanban — SA consulting firms"},
    },
    "Data Analyst": {
        "SQL":           {"priority": 5, "description": "Primary tool for all data work in SA"},
        "Excel":         {"priority": 4, "description": "Power Query, pivot tables — SA standard"},
        "Python":        {"priority": 4, "description": "pandas, matplotlib — growing fast"},
        "Power BI":      {"priority": 4, "description": "Most used BI tool in SA corporates"},
        "Statistics":    {"priority": 3, "description": "Descriptive stats, distributions"},
        "Data Cleaning": {"priority": 4, "description": "Real data is always messy"},
    },
    "Cybersecurity Analyst": {
        "Networking":   {"priority": 5, "description": "You must know TCP/IP cold"},
        "Linux":        {"priority": 5, "description": "Kali Linux, penetration testing"},
        "Python":       {"priority": 4, "description": "Scripting exploits and tools"},
        "Security+":    {"priority": 5, "description": "CompTIA Security+ is entry ticket"},
        "SIEM Tools":   {"priority": 3, "description": "Splunk, Microsoft Sentinel"},
        "Incident Response": {"priority": 4, "description": "SA companies pay well for this"},
    },
    "IT Support Specialist": {
        "Windows":          {"priority": 5, "description": "90% of SA offices run Windows"},
        "Networking":       {"priority": 4, "description": "LAN, WiFi, DNS, DHCP"},
        "CompTIA A+":       {"priority": 5, "description": "Gold standard entry cert in SA"},
        "Active Directory": {"priority": 3, "description": "User management in SA corps"},
        "Troubleshooting":  {"priority": 5, "description": "Your core daily skill"},
        "Communication":    {"priority": 4, "description": "User-facing role"},
    }
}
CERTIFICATIONS_DB = {
    "Microsoft AZ-900 Azure Fundamentals": {
        "provider": "Microsoft",
        "cost": "R2,700 (free vouchers via Microsoft events)",
        "cost_category": "low",
        "duration": "4-6 weeks self-study",
        "skill_area": "cloud azure aws networking",
        "link": "https://learn.microsoft.com/en-us/certifications/azure-fundamentals/",
        "description": "Best first cloud cert. Microsoft Learn study material is 100% free."
    },
    "AWS Cloud Practitioner": {
        "provider": "Amazon Web Services",
        "cost": "R1,800 (AWS offers free retakes via skill builder)",
        "cost_category": "low",
        "duration": "4-6 weeks self-study",
        "skill_area": "cloud aws",
        "link": "https://aws.amazon.com/certification/certified-cloud-practitioner/",
        "description": "Entry AWS cert. Free training at AWS Skill Builder."
    },
    "Google IT Support Certificate": {
        "provider": "Google via Coursera",
        "cost": "FREE for African learners",
        "cost_category": "free",
        "duration": "3-6 months part-time",
        "skill_area": "it support hardware networking windows troubleshooting",
        "link": "https://grow.google/intl/africa/",
        "description": "Completely free for SA learners. Covers networking, Python, OS, security."
    },
    "Google Data Analytics Certificate": {
        "provider": "Google via Coursera",
        "cost": "FREE for African learners",
        "cost_category": "free",
        "duration": "6 months part-time",
        "skill_area": "data analytics sql excel statistics data cleaning",
        "link": "https://grow.google/intl/africa/",
        "description": "Free for SA learners. SQL, data visualisation, spreadsheets, R."
    },
    "Python for Everybody": {
        "provider": "University of Michigan / Coursera",
        "cost": "Free to audit all content",
        "cost_category": "free",
        "duration": "8 weeks",
        "skill_area": "python programming",
        "link": "https://www.coursera.org/specializations/python",
        "description": "Best free Python course online. Click 'Audit' for all content at no cost."
    },
    "GitHub Foundations": {
        "provider": "GitHub / Microsoft",
        "cost": "Free",
        "cost_category": "free",
        "duration": "2-3 weeks",
        "skill_area": "git github version control ci/cd",
        "link": "https://learn.microsoft.com/en-us/training/github/",
        "description": "Free cert every developer should have. 100% online, immediately useful."
    },
    "Microsoft Learn SQL": {
        "provider": "Microsoft",
        "cost": "Free",
        "cost_category": "free",
        "duration": "20 hours",
        "skill_area": "sql database data systems",
        "link": "https://learn.microsoft.com/en-us/training/",
        "description": "Free SQL training. Great for SA banking and corporate jobs."
    },
    "CompTIA Security+": {
        "provider": "CompTIA",
        "cost": "R5,000 (look for vouchers on uCertify SA)",
        "cost_category": "medium",
        "duration": "2-3 months study",
        "skill_area": "security+ cybersecurity networking incident response",
        "link": "https://www.comptia.org/certifications/security",
        "description": "Most recognised entry security cert. SA financial sector loves this."
    },
    "CompTIA A+": {
        "provider": "CompTIA",
        "cost": "R3,500 per exam — 2 exams needed",
        "cost_category": "medium",
        "duration": "3-4 months study",
        "skill_area": "comptia a+ it support hardware windows troubleshooting",
        "link": "https://www.comptia.org/certifications/a",
        "description": "IT support gold standard. Widely recognised by SA employers."
    }
}
LEARNERSHIPS_DB = [
    {
        "name": "MICT SETA ICT Learnership",
        "organization": "MICT SETA (Government-funded)",
        "type": "Learnership",
        "duration": "12 months",
        "stipend": "R3,500 - R5,000/month",
        "province": "National",
        "remote": False,
        "required_skills": ["basic computer", "matric"],
        "application": "https://www.mict.org.za",
        "deadline": "Rolling applications — check site monthly",
        "description": "Government-funded ICT learnerships. SETA certificate on completion. No degree needed."
    },
    {
        "name": "IQ Business Systems Development Learnership",
        "organization": "IQ Business",
        "type": "Learnership",
        "duration": "12-24 months",
        "stipend": "Market related",
        "province": "Gauteng",
        "remote": False,
        "required_skills": ["python", "sql", "systems development", "java", "programming"],
        "application": "https://www.iqbusiness.net/careers",
        "deadline": "Annual intake — check LinkedIn",
        "description": "Top SA consulting firm. Real client projects from day one. Strong CV builder."
    },
    {
        "name": "AWS re/Start South Africa",
        "organization": "Amazon / Generation SA",
        "type": "Training Programme",
        "duration": "3 months full-time",
        "stipend": "Free training + job placement support",
        "province": "Gauteng, Cape Town",
        "remote": True,
        "required_skills": ["basic computer", "matric"],
        "application": "https://aws.amazon.com/training/restart/",
        "deadline": "Multiple intakes per year",
        "description": "Free full-time cloud training with AWS cert and job placement. Career changer."
    },
    {
        "name": "Umuzi Academy Tech Programme",
        "organization": "Umuzi",
        "type": "Learnership",
        "duration": "18 months",
        "stipend": "Paid stipend during programme",
        "province": "Gauteng",
        "remote": False,
        "required_skills": ["basic computer", "problem solving", "matric"],
        "application": "https://www.umuzi.org",
        "deadline": "Annual intake — applications open January",
        "description": "Specifically designed for township youth. Outstanding job placement rate."
    },
    {
        "name": "Capaciti Digital Skills Programme",
        "organization": "Capaciti",
        "type": "Graduate Programme",
        "duration": "12 months",
        "stipend": "R5,000 - R8,000/month",
        "province": "National",
        "remote": True,
        "required_skills": ["python", "programming", "data", "sql", "software development"],
        "application": "https://www.capaciti.org.za",
        "deadline": "Rolling applications",
        "description": "Connects graduates to corporates. Strong placement. Remote-friendly for SA."
    },
    {
        "name": "Explore AI Data Science Learnership",
        "organization": "Explore AI Academy",
        "type": "Learnership",
        "duration": "12 months",
        "stipend": "Paid — market related",
        "province": "National",
        "remote": True,
        "required_skills": ["python", "data", "statistics", "sql"],
        "application": "https://explore.ai",
        "deadline": "Rolling intake",
        "description": "Top data science learnership in SA. Real paid projects with SA companies."
    },
    {
        "name": "Microsoft LEAP Programme SA",
        "organization": "Microsoft South Africa",
        "type": "Internship",
        "duration": "6 months",
        "stipend": "Paid — competitive rate",
        "province": "Gauteng",
        "remote": False,
        "required_skills": ["programming", "cloud", "azure", "python", "software development"],
        "application": "https://careers.microsoft.com",
        "deadline": "Annual — watch LinkedIn for SA postings",
        "description": "Direct Microsoft engineering experience. Career-defining on any CV."
    },
    {
        "name": "WeThinkCode_ Programme",
        "organization": "WeThinkCode_",
        "type": "Training Programme",
        "duration": "2 years",
        "stipend": "Free tuition + corporate placement",
        "province": "Gauteng, Cape Town",
        "remote": False,
        "required_skills": ["logical thinking", "matric"],
        "application": "https://www.wethinkcode.co.za",
        "deadline": "Annual intake — applications open mid-year",
        "description": "Top free coding school. No prior experience needed. Peer-learning model."
    }
]