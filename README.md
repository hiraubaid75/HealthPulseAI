# HealthPulse AI — UAE Hospital Patient Experience Analyzer
<p align="center">
  <img src="https://raw.githubusercontent.com/hiraubaid75/HealthPulseAI/main/assets/banner.png" width="100%" />
</p>

End-to-end NLP-powered healthcare analytics project analyzing patient reviews from UAE hospitals using Python, HuggingFace, Topic Modeling, Streamlit, and Power BI.

🌟 Project Overview

HealthPulse AI is a complete Natural Language Processing (NLP) and Business Intelligence project designed to analyze thousands of patient reviews from UAE hospitals.

The project extracts insights on:

Service quality

Staff behaviour

Waiting times

Diagnosis quality

Billing issues

Patient satisfaction

This solution converts unstructured healthcare reviews into actionable insights to support hospital management, operational teams, and quality departments.

🚀 Key Features
✔ NLP Pipeline

Data Cleaning (text preprocessing)

Language Translation (Arabic → English)

Lemmatization

Sentiment Analysis (HuggingFace Transformer Model)

Topic Modeling

Keyword Extraction

Visualization & Insights

✔ Streamlit Web App

Multi-page analytics app with:

🏠 Home Page

📊 EDA Dashboard

☁️ WordClouds

🧠 Topic Insights

📬 Contact

✔ Power BI Dashboard

Professional visual dashboard showcasing:

KPI Summary

Ratings Distribution

Sentiment Trends

Topic Trends

Hospital-level Comparisons

✔ Fully Reproducible

Clean folder structure

requirements.txt included

Compatible with Windows/Linux/Mac

Can be deployed to Streamlit Cloud

🏥 Use Case: UAE Healthcare Industry

This project solves real challenges faced by:

Healthcare Quality Departments

Hospital CX Teams

Patient Experience Managers

Executive Management

Common insights include:

Identifying top reasons behind negative reviews

Understanding patient expectations

Monitoring hospital performance

Improving service delivery

Discovering department-level issues (billing, staff, waiting time, etc.)

📊 Technologies Used
Programming & NLP

Python

Pandas

NumPy

NLTK

WordCloud

HuggingFace Transformers

Matplotlib

Plotly

Visualization & BI

Power BI

Streamlit

Software & Tools

VS Code

Git / GitHub

Jupyter Notebook

Streamlit Cloud (for deployment)

📁 Project Structure

HealthPulseAI/
│── Streamlit/
│     ├── Home.py
│     ├── Pages/
│     │      ├── 1_EDA_Dashboard.py
│     │      ├── 2_WordCloud.py
│     │      ├── 3_Topic_Insights.py
│     │      └── 4_Contact.py
│     ├── data/
│     │      ├── hospital_reviews_final.csv
│
├── powerbi/
│     ├── dashboards.pbix
│
├── notebooks/
│     ├── HealthPulseAnalysis.ipynb
│
├── data/
│     ├── raw_reviews.csv
│     ├── cleaned_reviews.csv
│
├── outputs/
│     ├── model_outputs/
│     ├── visualizations/
│
├── requirements.txt
├── .gitignore
└── README.md

📈 Streamlit App Pages
🏠 Home Page

Overview of project, pipeline, dataset, and tech stack.

📊 EDA Dashboard

Rating distribution

Sentiment distribution

Hospital comparisons

Topic frequency

☁️ WordCloud Page

Positive wordcloud

Negative wordcloud

🧠 Topic Insights Page

Topic distribution

Sentiment score by topic

Top positive/negative topics

Topic keywords

📬 Contact Page

Email

LinkedIn

GitHub

WhatsApp (optional)

🧠 NLP Pipeline Details
1️⃣ Data Cleaning

Remove punctuation

Lowercasing

Remove stopwords

Lemmatization

2️⃣ Translation (Arabic → English)

Used Google Translate API to standardize text.

3️⃣ Sentiment Analysis

HuggingFace Transformer Model generates:

Sentiment Label (Positive / Negative)

Sentiment Score

4️⃣ Topic Modeling

Topics extracted from:

Keywords

Co-occurrence patterns

PCA-based clustering

5️⃣ Visualization

Power BI dashboards

Streamlit interactive charts

WordClouds

🖥️ How to Run the Streamlit App Locally
1. Clone the repository
   git clone https://github.com/hiraubaid75/HealthPulseAI.git
   cd HealthPulseAI
2. Create Virtual Environment
   python -m venv venv
3. Activate venv
   venv\Scripts\activate
4. Install Requirements
   pip install -r requirements.txt
5. Run Streamlit App
   cd Streamlit
   streamlit run Home.py

🌐 Deployment

Deploy for FREE on:

👉 Streamlit Cloud

Login with GitHub

Connect this repo

Select Streamlit/Home.py

Deploy

https://healthpulseai.streamlit.app

📩 Contact

📧 Email: hiraubaid95@gmail.com

🔗 LinkedIn: https://linkedin.com/in/hira-barlas

🐙 GitHub: https://github.com/hiraubaid75

💬 WhatsApp: wa.me/971554072324

⭐ If you like this project, give it a star on GitHub!

Your support helps me grow as a Data Analyst & AI Engineer 😊

---

## 📸 Power BI Dashboard Screenshots

### **📊 Page 1 — Executive Summary**
Overview of key patient experience KPIs across UAE hospitals.

![Page 1 — Executive Summary](powerbi/ScreenShots/Page%201%20%E2%80%94%20Executive%20Summary.png)

---

### **📊 Page 2 — Detailed Insights**
Topic-wise insights, sentiment breakdown, and review analysis.

![Page 2 — Detailed Insights](powerbi/ScreenShots/Page%202_Detailed%20Insights.png)

---

### **📊 Page 3 — Hospital Comparison**
Hospital-level comparison of ratings, sentiment scores, and topics.

![Page 3 — Hospital Comparison](powerbi/ScreenShots/Page%203_Hospital%20Comparison.png)

---




