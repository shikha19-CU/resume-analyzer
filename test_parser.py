from text_cleaner import clean_text
from match_score import calculate_similarity

# Example data that should match well
resume_text = """
Shikha is a data scientist skilled in Python, machine learning, data visualization using Tableau, and NLP. 
Worked on scikit-learn and deep learning models.
"""

jd_text = """
Looking for a data scientist with experience in Python, machine learning, NLP, Tableau, and data analysis.
Knowledge of scikit-learn and deep learning is a bonus.
"""

cleaned_resume = clean_text(resume_text)
cleaned_jd = clean_text(jd_text)

print("Cleaned Resume:", cleaned_resume)
print("Cleaned JD:", cleaned_jd)

score = calculate_similarity(cleaned_resume, cleaned_jd)
print(f"✅ Match Score: {score}%")
