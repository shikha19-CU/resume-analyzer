import streamlit as st
from resume_parser import extract_text_from_pdf
from text_cleaner import clean_text
from match_score import calculate_similarity

st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.title("📄 Resume Analyzer using NLP & ML")
st.write("Upload your resume and paste a job description to check how well your resume matches!")

# Upload PDF
uploaded_file = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])

# Paste Job Description
jd_text = st.text_area("Paste the Job Description here")

if uploaded_file and jd_text:
    with st.spinner("Analyzing your resume..."):
        # Extract and clean
        resume_text = extract_text_from_pdf(uploaded_file)
        cleaned_resume = clean_text(resume_text)
        cleaned_jd = clean_text(jd_text)

        # 🧪 Debugging: Show text lengths
        st.write(f"📏 Resume Length: {len(cleaned_resume)} characters")
        st.write(f"📏 JD Length: {len(cleaned_jd)} characters")

        # Match
        score = calculate_similarity(cleaned_resume, cleaned_jd)

        # Show result
        st.success(f"✅ Match Score: {score}%")


        if score >= 75:
            st.info("👍 Great! Your resume matches well with the job description.")
        elif 50 <= score < 75:
            st.warning("⚠️ Not bad, but you may want to tailor your resume more.")
        else:
            st.error("❌ Your resume doesn't match well. Try adding relevant skills/experience.")
