🏥 HealthPulse AI — UAE Hospital Patient Experience Analyzer
<p align="center"> <img src="https://raw.githubusercontent.com/hiraubaid75/HealthPulseAI/main/assets/banner.png" width="100%" /> </p> <p align="center"><b> End-to-end NLP-powered healthcare analytics project analyzing patient reviews from UAE hospitals using Python, HuggingFace, Topic Modeling, Streamlit, and Power BI. </b></p>
<p align="center"> <!-- Streamlit Demo Button (Dummy Link for Now) --> <a href="https://healthpulseai-demo.streamlit.app" target="_blank"> <img src="https://img.shields.io/badge/▶️%20Open%20Streamlit%20Demo-0A66C2?style=for-the-badge&logo=streamlit&logoColor=white" /> </a> <!-- Power BI Screenshots --> <a href="https://github.com/hiraubaid75/HealthPulseAI/tree/main/powerbi/ScreenShots" target="_blank"> <img src="https://img.shields.io/badge/📊%20Power%20BI%20Screenshots-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" /> </a> <!-- GitHub Repo --> <a href="https://github.com/hiraubaid75/HealthPulseAI" target="_blank"> <img src="https://img.shields.io/badge/GitHub%20Repo-181717?style=for-the-badge&logo=github&logoColor=white" /> </a> </p>
<p align="center"> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/> <img src="https://img.shields.io/badge/HuggingFace-FCC624?style=for-the-badge&logo=huggingface&logoColor=black"/> <img src="https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black"/> <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white"/> </p>
📚 Table of Contents

Project Overview

Key Features

Live Demo

Project Structure

NLP Pipeline Details

Streamlit App Pages

Power BI Dashboard Screenshots

How to Run Locally

Technologies Used

Recruiter Notes

Contact

⭐ Project Overview

HealthPulse AI is a full NLP + BI solution designed to analyze thousands of patient reviews from UAE hospitals.

It extracts insights about:

⭐ Service quality

⭐ Staff behaviour

⭐ Waiting times

⭐ Diagnosis accuracy

⭐ Billing issues

⭐ Patient satisfaction

This project converts unstructured text into actionable insights to support:

Hospital CX teams

Quality departments

Executive leadership

Healthcare decision makers

🚀 Key Features
✔ NLP Pipeline

Text cleaning

Translation (Arabic → English)

Lemmatization

HuggingFace transformer sentiment model

Topic modeling

Keyword extraction

✔ Streamlit App

Interactive dashboards

Topic-wise sentiment

Word clouds

Hospital comparisons

✔ Power BI Dashboards

Executive Summary

Detailed topic insights

Hospital comparison

🔗 Live Demo

🌐 Streamlit Demo (Dummy Link — Update after Deployment)
👉 https://healthpulseai-demo.streamlit.app

📁 Project Structure
HealthPulseAI/
├── Streamlit/
│   ├── Home.py
│   ├── Pages/
│   │   ├── 1_EDA_Dashboard.py
│   │   ├── 2_WordCloud.py
│   │   ├── 3_Topic_Insights.py
│   │   └── 4_Contact.py
│   ├── data/
│   │   └── hospital_reviews_final.csv
│   └── assets/
│       └── images, icons
│
├── powerbi/
│   ├── dashboards.pbix
│   └── ScreenShots/
│       ├── Page1_ExecutiveSummary.png
│       ├── Page2_DetailedInsights.png
│       └── Page3_HospitalComparison.png
│
├── notebooks/
│   └── HealthPulseAnalysis.ipynb
│
├── data/
│   ├── raw_reviews.csv
│   └── cleaned_reviews.csv
│
├── outputs/
│   ├── model_outputs/
│   └── visualizations/
│
├── assets/
│   ├── banner.png
│   └── logos/
│
├── requirements.txt
└── README.md

🧠 NLP Pipeline Details
1️⃣ Data Cleaning

Remove special characters

Lowercase

Remove stopwords

Lemmatization

2️⃣ Translation

Arabic reviews → English (Google Translate API)

3️⃣ Sentiment Analysis

HuggingFace Transformer Model

Produces:

Sentiment_Label (POSITIVE / NEGATIVE)

Sentiment_Score (0–1)

4️⃣ Topic Modeling

Keyword extraction

Clustering

Topic labels & keywords

5️⃣ Visualization

Power BI

Streamlit

WordClouds

📸 Streamlit App Pages
🏠 Home Page

Overview of the hospitals and project purpose.

📊 EDA Dashboard

Rating distribution

Sentiment breakdown

Topic frequency

Hospital-level stats

☁️ WordCloud Page

Positive word cloud

Negative word cloud

🧠 Topic Insights

Topic distribution

Sentiment score per topic

Top positive/negative topics

Keywords per topic

📬 Contact Page

Links to Email, GitHub, LinkedIn, WhatsApp

🖥️ Power BI Dashboard Screenshots
📊 Page 1 — Executive Summary

📊 Page 2 — Detailed Insights

📊 Page 3 — Hospital Comparison

⚙️ How to Run Locally
# 1. Clone the repo
git clone https://github.com/hiraubaid75/HealthPulseAI.git
cd HealthPulseAI

# 2. Create virtual environment
python -m venv venv

# 3. Activate
venv\Scripts\activate

# 4. Install requirements
pip install -r requirements.txt

# 5. Run Streamlit app
cd Streamlit
streamlit run Home.py

🛠 Technologies Used
Programming & NLP

Python

Pandas

NumPy

NLTK

HuggingFace Transformers

WordCloud

Plotly

BI & Visualization

Power BI

Streamlit

Tools

VS Code

Git / GitHub

Jupyter Notebook

Streamlit Cloud

🧑‍💼 Recruiter Notes

This project demonstrates:

✔ End-to-end NLP pipeline
✔ SQL/Python/Power BI integration
✔ Dashboard storytelling
✔ Cloud deployment
✔ Real-world UAE healthcare use case

This reflects strong skills in Data Analysis, NLP, BI dashboards, and App Development.

📩 Contact

📧 Email — hiraubaid95@gmail.com

🔗 LinkedIn — https://linkedin.com/in/hira-barlas

🐙 GitHub — https://github.com/hiraubaid75

💬 WhatsApp — wa.me/971554072324

⭐ If you like this project, please star the repo!
