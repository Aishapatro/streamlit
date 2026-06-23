import streamlit as st
import pdfplumber

st.set_page_config(page_title="AI Resume Analyzer")

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)", type=["pdf"]
)

if uploaded_file is not None:
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()

    st.subheader("Resume Content")
    st.write(text)

    skills = [
        "Python", "Java", "C++", "SQL",
        "Machine Learning", "Data Analysis",
        "Pandas", "NumPy", "Streamlit"
    ]

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    st.subheader("Detected Skills")
    st.write(found_skills)

    score = len(found_skills) * 10
    score = min(score, 100)

    st.subheader("Resume Score")
    st.progress(score)
    st.write(f"Score: {score}/100")

    if score < 50:
        st.warning(
            "Add more technical skills and projects."
        )
    else:
        st.success(
            "Good Resume! Keep improving."
        )
