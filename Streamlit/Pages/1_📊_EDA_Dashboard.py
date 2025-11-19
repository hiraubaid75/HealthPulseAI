import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="EDA Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 EDA Dashboard")
st.write("Explore review trends, ratings, sentiment distribution and hospital comparisons.")

# Load dataset
df = pd.read_csv("data/hospital_reviews_final.csv")

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Reviews", len(df))
col2.metric("Avg Rating", round(df["rating"].mean(), 2))
col3.metric("Avg Sentiment Score", round(df["Sentiment_Score"].mean(), 2))
col4.metric("Hospitals", df["hospital"].nunique())

st.markdown("---")

# Rating Distribution
st.subheader("⭐ Rating Distribution")
fig1 = px.histogram(df, x="rating", nbins=5)
st.plotly_chart(fig1, use_container_width=True)

# Sentiment Distribution
st.subheader("💬 Sentiment Distribution")
fig2 = px.histogram(df, x="Sentiment_Label")
st.plotly_chart(fig2, use_container_width=True)

# Reviews by Hospital
st.subheader("🏥 Review Count by Hospital")
fig3 = px.bar(df["hospital"].value_counts())
st.plotly_chart(fig3, use_container_width=True)

# Topic Distribution
st.subheader("🧵 Common Topics")
fig4 = px.bar(df, x="Topic_Name")
st.plotly_chart(fig4, use_container_width=True)
