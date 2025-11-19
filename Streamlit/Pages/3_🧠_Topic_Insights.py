import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Topic Insights",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Topic & Sentiment Insights")
st.write("Detailed breakdown of topics, sentiment, and hospital performance.")


# Load dataset
df = pd.read_csv("data/hospital_reviews_final.csv")

st.markdown("### 🔍 Select a Hospital")
hospital_list = ["All"] + sorted(df["hospital"].unique())
selected_hospital = st.selectbox("", hospital_list)

# Filter by hospital
if selected_hospital != "All":
    df = df[df["hospital"] == selected_hospital]


# ======================================================
# 1️⃣ TOP POSITIVE TOPICS
# ======================================================
st.subheader("🌿 Top Positive Topics")

pos_df = df[df["Sentiment_Label"] == "POSITIVE"]
if len(pos_df) > 0:
    fig_pos = px.bar(
        pos_df["Topic_Name"].value_counts().reset_index(),
        x="Topic_Name", y="count",
        labels={"Topic_Name": "Topic", "count": "Count"},
        color="count"
    )
    st.plotly_chart(fig_pos, use_container_width=True)
else:
    st.warning("No positive topics found for this selection.")


# ======================================================
# 2️⃣ TOP NEGATIVE TOPICS
# ======================================================
st.subheader("🔥 Top Negative Topics")

neg_df = df[df["Sentiment_Label"] == "NEGATIVE"]
if len(neg_df) > 0:
    fig_neg = px.bar(
        neg_df["Topic_Name"].value_counts().reset_index(),
        x="Topic_Name", y="count",
        labels={"Topic_Name": "Topic", "count": "Count"},
        color="count"
    )
    st.plotly_chart(fig_neg, use_container_width=True)
else:
    st.warning("No negative topics found for this selection.")


# ======================================================
# 3️⃣ TOPIC DISTRIBUTION
# ======================================================
st.subheader("📦 Overall Topic Distribution")

fig_dist = px.bar(
    df["Topic_Name"].value_counts().reset_index(),
    x="Topic_Name", y="count",
    labels={"Topic_Name": "Topic", "count": "Count"},
    color="count"
)
st.plotly_chart(fig_dist, use_container_width=True)


# ======================================================
# 4️⃣ SENTIMENT SCORE BY TOPIC
# ======================================================
st.subheader("📊 Average Sentiment Score by Topic")

topic_score = df.groupby("Topic_Name")["Sentiment_Score"].mean().reset_index()
fig_score = px.bar(
    topic_score,
    x="Topic_Name", y="Sentiment_Score",
    color="Sentiment_Score"
)
st.plotly_chart(fig_score, use_container_width=True)


# ======================================================
# 5️⃣ TOPIC KEYWORDS TABLE
# ======================================================
st.subheader("📝 Topic Keywords")

keyword_df = df[["Topic_Name", "Topic_Keywords"]].drop_duplicates()
st.dataframe(keyword_df, use_container_width=True)
