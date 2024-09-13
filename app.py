from flask import Flask, render_template, request

app = Flask(__name__)

# Job and skills data
jobs = {
    "Full-Stack Developer": ["JavaScript (React or Angular)", "Node.js", "SQL or MongoDB", "Git", "REST APIs"],
    "Data Scientist": ["Python (Pandas, NumPy)", "Machine Learning", "SQL", "Data Visualization (Power BI, Tableau)", "Statistics"],
    "DevOps Engineer": ["Docker", "Kubernetes", "AWS or Azure", "Jenkins (CI/CD)", "Linux"],
    "Mobile Application Developer": ["Swift (iOS) or Kotlin (Android)", "REST APIs", "React Native or Flutter", "SQLite", "Firebase"],
    "Software Engineer": ["DSA", "SDLC", "Web development", "API & Web Services"],
    "AI/ML Engineer": ["Python (TensorFlow, PyTorch)", "Machine Learning", "Data Structures & Algorithms", "Model Optimization", "Cloud AI Services (AWS, Google Cloud)"],
    "Cloud Engineer": ["AWS (EC2, S3)", "Kubernetes", "Docker", "Networking", "Terraform"],
    "Cybersecurity Specialist": ["Penetration Testing", "Network Security", "Encryption", "Firewalls & VPNs", "Incident Response"],
    "Software Tester (QA Engineer)": ["Selenium", "Test Automation (JUnit, TestNG)", "Java or Python for Testing", "Jenkins (CI/CD)"],
    "Blockchain Developer": ["Solidity (Smart Contracts)", "Ethereum", "Cryptography", "Node.js", "Web3.js"],
    "Game Developer": ["C# (Unity) or C++ (Unreal Engine)", "Game Physics", "3D Modeling (Blender, Maya)", "JavaScript (WebGL)"],
    "Data Engineer": ["Python (Pandas)", "SQL", "Spark or Kafka", "ETL Pipelines", "AWS or GCP Data Tools"],
    "Backend Developer": ["Node.js or Python (Django/Flask)", "SQL (PostgreSQL or MySQL)", "REST APIs", "Microservices", "Docker"],
    "UI/UX Designer": ["HTML, CSS", "JavaScript (React or Vue.js)", "Figma or Sketch", "User Research", "Responsive Design"],
    "AI/ML Researcher": ["Python (TensorFlow, Keras)", "Deep Learning", "Data Structures", "Model Optimization"],
    "Database Administrator": ["SQL (MySQL, PostgreSQL)", "Database Security", "Backup and Recovery", "Performance Tuning"],
    "Data Analyst": ["Python", "Power BI", "Statistical Analysis", "Tableau", "R", "SQL"],
    "Network Engineer": ["Cloud Networking", "Wireless Networking", "Network Configuration"],
    "Front-end Developer": ["HTML", "CSS", "JavaScript", "Front-end Frameworks"]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/skills-for-job', methods=['GET', 'POST'])
def skills_for_job():
    if request.method == 'POST':
        job_selected = request.form['job']
        skills = jobs.get(job_selected, [])
        return render_template('skills_for_job.html', job=job_selected, skills=skills, jobs=jobs.keys())
    return render_template('skills_for_job.html', jobs=jobs.keys())

@app.route('/jobs-for-skills', methods=['GET', 'POST'])
def jobs_for_skills():
    skills = set(skill for skill_list in jobs.values() for skill in skill_list)
    selected_skills = []
    matched_jobs = []
    additional_skills = {}

    if request.method == 'POST':
        selected_skills = request.form.getlist('skills')
        skill_match_counts = {}

        # Find jobs with matching skills
        for job, job_skills in jobs.items():
            match_count = len(set(selected_skills) & set(job_skills))
            if match_count > 0:
                skill_match_counts[job] = match_count

        # Sort jobs based on the number of matching skills
        matched_jobs = sorted(skill_match_counts, key=skill_match_counts.get, reverse=True)

        # Find additional skills needed for each matched job
        for job in matched_jobs:
            job_skills = jobs[job]
            missing_skills = set(job_skills) - set(selected_skills)
            if missing_skills:
                additional_skills[job] = missing_skills

    return render_template('jobs_for_skills.html', skills=skills, selected_skills=selected_skills, matched_jobs=matched_jobs, additional_skills=additional_skills)

if __name__ == '__main__':
    app.run(debug=True)
