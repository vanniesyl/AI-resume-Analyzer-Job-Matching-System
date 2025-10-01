import streamlit as st
import pandas as pd
import PyPDF2
import docx2txt
from sentence_transformers import SentenceTransformer, util
import plotly.express as px
import plotly.graph_objects as go
import re
import tempfile
import os
import base64

# -----------------------------
# Page Setup
# -----------------------------
st.set_page_config(layout="wide")
st.title("💼 AI Resume Analyzer & Professional Candidate Dashboard")

# -----------------------------
# Resume Upload & Job Description
# -----------------------------
uploaded_files = st.file_uploader(
    "Upload Single or Multiple Resumes (PDF/DOCX)", 
    type=['pdf','docx'], 
    accept_multiple_files=True
)
job_description = st.text_area("Enter Job Description", height=150)
years_exp = st.number_input("Enter Candidate Experience (Years)", min_value=0, max_value=30, value=5)

if uploaded_files and job_description:

    # -----------------------------
    # Skill Taxonomy & Domain Expertise
    # -----------------------------
    skill_taxonomy = ["Python", "SQL", "Data Analysis", "Tableau", "Machine Learning", 
                      "Power BI", "AWS", "Excel", "R", "Statistics", "Communication", 
                      "Leadership", "Marketing", "Finance", "Business Intelligence"]

    domain_expertise = {"Finance": 0.7, "Marketing": 0.5, "Business Intelligence": 0.8}

    # -----------------------------
    # NLP Model
    # -----------------------------
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # -----------------------------
    # Functions
    # -----------------------------
    def extract_text(file):
        if file.name.endswith(".pdf"):
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + " "
            return text
        elif file.name.endswith(".docx"):
            return docx2txt.process(file)
        else:
            return ""

    def extract_skills(text, taxonomy):
        return [skill for skill in taxonomy if re.search(r'\b'+re.escape(skill.lower())+r'\b', text.lower())]

    # -----------------------------
    # Process Resumes
    # -----------------------------
    candidates = []
    for uploaded_file in uploaded_files:
        resume_text = extract_text(uploaded_file)
        resume_skills = extract_skills(resume_text, skill_taxonomy)
        jd_skills = extract_skills(job_description, skill_taxonomy)
        matched_skills = list(set(resume_skills) & set(jd_skills))
        missing_skills = list(set(jd_skills) - set(resume_skills))
        job_fit_score = util.cos_sim(model.encode(resume_text), model.encode(job_description)).item()

        candidates.append({
            "Resume": uploaded_file.name,
            "Matched Skills": matched_skills,
            "Missing Skills": missing_skills,
            "Job Fit Score": job_fit_score,
            "Resume Text": resume_text
        })

    # -----------------------------
    # KPI Section
    # -----------------------------
    selected_candidate = st.selectbox("Select Resume", [c['Resume'] for c in candidates])
    cand = next(c for c in candidates if c['Resume'] == selected_candidate)

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Similarity Score 🔗", f"{int(cand['Job Fit Score']*100)}%")
    col2.metric("Matched Skills ✅", len(cand['Matched Skills']), delta=f"{len(cand['Missing Skills'])} missing")
    col3.metric("Missing Skills ⚠️", len(cand['Missing Skills']))
    col4.metric("Experience 🎯", f"{years_exp} yrs")
    col5.metric("Job Fit 💯", f"{int(cand['Job Fit Score']*100)}% 🔥")

    # -----------------------------
    # Skill Bar Chart
    # -----------------------------
    skill_df = pd.DataFrame({
        "Skill": skill_taxonomy,
        "Matched": [1 if s in cand['Matched Skills'] else 0 for s in skill_taxonomy]
    })
    fig_bar = px.bar(skill_df, x="Skill", y="Matched", color="Matched", 
                     color_continuous_scale=['red','green'], title="Skill Coverage")
    fig_bar.update_layout(yaxis=dict(tickvals=[0,1], ticktext=['Missing','Matched']))
    st.plotly_chart(fig_bar, use_container_width=True)

    # -----------------------------
    # Skill Radar Chart
    # -----------------------------
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=[1 if s in cand['Matched Skills'] else 0 for s in skill_taxonomy],
        theta=skill_taxonomy,
        fill='toself',
        marker_color='green'
    ))
    fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0,1])),
                            showlegend=False,
                            title="Skill Match Radar")
    st.plotly_chart(fig_radar, use_container_width=True)

    # -----------------------------
    # Candidate Summary Card
    # -----------------------------
    st.subheader("📄 Candidate Summary")
    st.markdown(f"""
    <div style='padding:10px; border:2px solid #4CAF50; border-radius:10px; background-color:#f0f9f0'>
    - Experience: {years_exp} yrs 🎯  
    - Strong Skills: <span style='color:green'>{', '.join(cand['Matched Skills'])}</span> ✅  
    - Skills to Improve:<span style='color:red'>{', '.join(cand['Missing Skills'])}</span> ⚠️  
    - Overall Job Fit:<span style='color:blue'>{'High 🔥' if cand['Job Fit Score']>0.7 else 'Medium ⚠️'}</span>
    </div>
    """, unsafe_allow_html=True)

    # -----------------------------
    # Skill Suggestions
    # -----------------------------
    st.subheader("💡 Skill Improvement Suggestions")
    for skill in cand['Missing Skills']:
        st.markdown(f"🔹 {skill}")

    # -----------------------------
    # Domain Expertise Progress Bars
    # -----------------------------
    st.subheader("🏷️ Domain Expertise")
    for domain, score in domain_expertise.items():
        st.progress(int(score*100))
        st.write(f"{domain}: {int(score*100)}% match")

    # -----------------------------
    # PDF Export (Optional)
    # -----------------------------
    st.subheader("📥 Export Candidate Summary to PDF")

if st.button("Generate PDF"):

    # Save bar and radar charts as images
    tmp_bar = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    tmp_radar = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    fig_bar.write_image(tmp_bar.name, width=800, height=400)
    fig_radar.write_image(tmp_radar.name, width=800, height=400)

    # Generate HTML content for PDF
    html_content = f"""
    <h1>Candidate Summary</h1>
    <p><strong>Resume:</strong> {cand['Resume']}</p>
    <p><strong>Job Fit Score:</strong> {int(cand['Job Fit Score']*100)}%</p>

    <h2>Matched Skills ✅</h2>
    <p>{', '.join(cand['Matched Skills']) if cand['Matched Skills'] else 'None'}</p>

    <h2>Skills to Improve ⚠️</h2>
    <p>{', '.join(cand['Missing Skills']) if cand['Missing Skills'] else 'None'}</p>

    <h2>Skill Bar Chart</h2>
    <img src="{tmp_bar.name}" width="700"/>

    <h2>Skill Radar Chart</h2>
    <img src="{tmp_radar.name}" width="700"/>

    <h2>Job Recommendations 💡</h2>
    <ul>
    {"".join([f"<li>{skill}</li>" for skill in cand['Missing Skills']])}
    </ul>
    """

    # Generate PDF
    pdf_file = f"{cand['Resume']}_Summary.pdf"
    pdfkit.from_string(html_content, pdf_file)

    # Provide download link
    with open(pdf_file, "rb") as f:
        pdf_bytes = f.read()
        b64 = base64.b64encode(pdf_bytes).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="{pdf_file}">📥 Download PDF</a>'
        st.markdown(href, unsafe_allow_html=True)