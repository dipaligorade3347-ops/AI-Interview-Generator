def interview_prompt(role, experience, skills):
    return f"""
Act as a senior interviewer.

Role: {role}
Experience: {experience}
Skills: {skills}

Generate:
1. 10 Technical Questions
2. 5 HR Questions
3. Expected Answer Points
"""