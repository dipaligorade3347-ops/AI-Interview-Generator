
import streamlit as st
import google.generativeai as genai
from fpdf import FPDF

# ==========================
# GEMINI API KEY
# ==========================

API_KEY = "YOUR API-KEY"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# ==========================
# APP TITLE
# ==========================

st.title("AI Interview Generator & Evaluator")

# ==========================
# QUESTION GENERATOR
# ==========================

st.header("Interview Question Generator")

role = st.selectbox(
    "Select Role",
    ["Data Analyst", "AI Engineer", "Python Developer"]
)

experience = st.selectbox(
    "Experience Level",
    ["Fresher", "1-2 Years", "3+ Years"]
)

difficulty = st.selectbox(
    "Difficulty Level",
    ["Easy", "Medium", "Hard"]
)

company = st.selectbox(
    "Target Company",
    ["General", "TCS", "Infosys", "Accenture", "Capgemini"]
)

skills = st.text_area(
    "Enter Skills",
    placeholder="Python, SQL, Power BI"
)

if st.button("Generate Questions"):

    prompt = f"""
    Act as a senior interviewer.

    Role: {role}
    Experience: {experience}
    Difficulty: {difficulty}
    Target Company: {company}

    Skills:
    {skills}

    Generate:

    10 Technical Questions
    5 HR Questions

    Format properly.
    """

    response = model.generate_content(prompt)

    st.subheader("Generated Questions")

    st.write(response.text)

# ==========================
# ANSWER EVALUATION
# ==========================

st.header("Answer Evaluation")

question = st.text_input(
    "Enter Question"
)

answer = st.text_area(
    "Enter Your Answer"
)

if st.button("Evaluate Answer"):

    eval_prompt = f"""
    Act as a senior technical interviewer.

    Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate the answer and provide:

    1. Score out of 10
    2. Strengths
    3. Weaknesses
    4. Improved Answer
    """

    response = model.generate_content(eval_prompt)

    evaluation_result = response.text

    st.subheader("Evaluation Result")

    st.write(evaluation_result)

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.multi_cell(
        0,
        10,
        f"""
Question:
{question}

Answer:
{answer}

Evaluation:
{evaluation_result}
"""
    )

    pdf.output("Interview_Report.pdf")

    with open("Interview_Report.pdf", "rb") as file:
        st.download_button(
            label="Download PDF Report",
            data=file,
            file_name="Interview_Report.pdf",
            mime="application/pdf"
        )

