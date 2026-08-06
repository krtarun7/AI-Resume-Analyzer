import re

# ==========================================================
# Master Skill List
# ==========================================================

SKILLS = [

    # Programming Languages
    "java", "python", "c", "c++", "c#", "javascript", "typescript",
    "php", "ruby", "go", "golang", "swift", "kotlin", "scala",
    "rust", "r", "matlab", "perl", "dart",

    # Frontend
    "html", "css", "bootstrap", "tailwind", "material ui",
    "react", "reactjs", "next.js", "nextjs", "angular",
    "vue", "vue.js", "jquery", "redux",

    # Backend
    "node.js", "nodejs", "express", "express.js",
    "spring", "spring boot", "hibernate",
    "servlet", "jsp",
    "fastapi", "django", "flask",
    ".net", "asp.net", "laravel",

    # Mobile
    "android", "ios", "flutter", "react native",

    # Database
    "mysql", "postgresql", "mongodb", "sqlite",
    "oracle", "sql server", "redis",
    "firebase", "cassandra", "dynamodb",

    # Cloud
    "aws", "amazon web services",
    "azure", "gcp", "google cloud",

    # DevOps
    "docker", "kubernetes", "jenkins",
    "terraform", "ansible",
    "github actions", "gitlab ci",
    "ci/cd", "devops",

    # Version Control
    "git", "github", "bitbucket",

    # API
    "rest api", "restful api",
    "graphql", "soap",

    # Java
    "jdbc", "jpa", "maven", "gradle",
    "lombok", "spring security",
    "microservices",

    # Python
    "numpy", "pandas", "matplotlib",
    "seaborn", "scipy",
    "scikit-learn", "opencv",

    # AI / ML
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "tensorflow",
    "keras",
    "pytorch",
    "nlp",
    "computer vision",
    "llm",
    "transformers",
    "langchain",
    "huggingface",
    "openai",
    "gemini",

    # Data Analytics
    "power bi",
    "tableau",
    "excel",
    "data analysis",
    "data visualization",

    # Testing
    "junit",
    "mockito",
    "pytest",
    "selenium",
    "postman",

    # Networking
    "tcp/ip",
    "dns",
    "dhcp",
    "routing",
    "switching",
    "firewall",
    "vpn",
    "osi",
    "ccna",

    # Cyber Security
    "penetration testing",
    "ethical hacking",
    "wireshark",
    "burp suite",
    "nmap",
    "owasp",

    # Linux
    "linux",
    "ubuntu",
    "unix",
    "shell scripting",
    "bash",

    # Tools
    "jira",
    "figma",
    "eclipse",
    "intellij",
    "vscode",
    "visual studio",

    # Soft Skills
    "leadership",
    "communication",
    "teamwork",
    "problem solving",
    "critical thinking",
    "time management",
    "adaptability",

    # DSA
    "data structures",
    "algorithms",
    "oop",
    "object oriented programming",

    # Misc
    "agile",
    "scrum",
    "kanban",
    "json",
    "xml",
    "yaml",

    # Big Data
    "hadoop",
    "spark",
    "kafka",

    # Containers
    "podman",

    # Security
    "oauth",
    "jwt",

    # Monitoring
    "grafana",
    "prometheus",

    # Message Brokers
    "rabbitmq",
    "apache kafka",

    # Operating Systems
    "windows",
    "macos",

    # Embedded
    "arduino",
    "raspberry pi"
]


# ==========================================================
# Extract Skills
# ==========================================================

def extract_skills(text):
    """
    Extract technical skills from text.
    """

    text = text.lower()

    # Normalize common variations
    replacements = {
        "reactjs": "react",
        "nodejs": "node.js",
        "nextjs": "next.js",
        "springboot": "spring boot",
        "expressjs": "express",
        "restful api": "rest api",
        "google cloud platform": "gcp",
        "amazon web services": "aws"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    found = set()

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found.add(skill)

    return sorted(found)


# ==========================================================
# Compare Resume vs Job Description
# ==========================================================

def compare_skills(resume_text, job_description):
    """
    Compare resume skills with job description skills.
    """

    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(job_description))

    matched = sorted(resume_skills.intersection(jd_skills))
    missing = sorted(jd_skills.difference(resume_skills))

    return {
        "matched_skills": matched,
        "missing_skills": missing
    }