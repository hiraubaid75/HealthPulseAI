import streamlit as st
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)
import os
import pandas as pd

file_path = os.path.join("data", "hospital_reviews_final.csv")
df = pd.read_csv(file_path)


# ---------------------
# PAGE CONFIG
# ---------------------


# ---------------------
# HOME TITLE
# ---------------------
st.title("🏠 Home")
st.markdown("### 💜 HealthPulse AI — UAE Hospital Patient Experience Analyzer")

st.markdown("---")

# ---------------------
# ABOUT THE PROJECT
# ---------------------
st.header("🌟 About This Project")

st.write("""
HealthPulse AI is an end-to-end **NLP-powered healthcare analytics project**
designed to analyze patient reviews from UAE hospitals.

It converts raw patient feedback into actionable insights using:
- Data Cleaning  
- Translation (Arabic → English)  
- Sentiment Analysis  
- Topic Modeling  
- Power BI Dashboard  
- Streamlit Web App  
""")

# ---------------------
# YOUR ROLE
# ---------------------
st.header("👩‍💻 My Role")
st.write("""
**Data Analyst | NLP Specialist**

I performed:
- Data preprocessing  
- Text cleaning & lemmatization  
- Translation  
- HuggingFace sentiment analysis  
- Topic modeling  
- Power BI dashboard creation  
- Web app development  
""")


# ---------------------
# DATASET INFO
# ---------------------
st.header("📘 Dataset Overview")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Reviews", "300+")
    st.metric("Hospitals", "3")
with col2:
    st.metric("NLP Columns", "12+")
    st.metric("Languages", "Arabic + English")

# ---------------------
# NLP PIPELINE
# ---------------------
st.header("🧠 NLP Pipeline")

st.write("""
1️⃣ Data Cleaning  
2️⃣ Translation  
3️⃣ Sentiment Analysis  
4️⃣ Topic Modeling  
5️⃣ Visualization  
""")

# ---------------------
# TECH STACK
# ---------------------
st.header("🛠 Tech Stack")

st.write("""
- Python  
- Pandas  
- HuggingFace Transformers  
- Matplotlib  
- WordCloud  
- Power BI  
- Streamlit  
""")

st.markdown("---")
st.success("Use the left sidebar to navigate through the dashboard, wordclouds, topic insights, and contact page.")