import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import pandas as pd

file_path = os.path.join("data", "hospital_reviews_final.csv")
df = pd.read_csv(file_path)


st.set_page_config(
    page_title="WordCloud",
    page_icon="☁️",
    layout="wide"
)

st.title("☁️ WordClouds")
st.write("Visualize the most common words in positive and negative reviews.")

# Load dataset
df = pd.read_csv("data/hospital_reviews_final.csv")

# Filter text
positive_text = " ".join(df[df["Sentiment_Label"] == "POSITIVE"]["lemmatized_text"].astype(str))
negative_text = " ".join(df[df["Sentiment_Label"] == "NEGATIVE"]["lemmatized_text"].astype(str))

col1, col2 = st.columns(2)

# Positive WordCloud
with col1:
    st.subheader("🌿 Positive Reviews WordCloud")

    if positive_text.strip():
        pos_wc = WordCloud(width=600, height=400, background_color="white").generate(positive_text)
        fig1, ax1 = plt.subplots(figsize=(6,4))
        ax1.imshow(pos_wc, interpolation='bilinear')
        ax1.axis("off")
        st.pyplot(fig1)
    else:
        st.warning("No positive reviews found.")

# Negative WordCloud
with col2:
    st.subheader("🔥 Negative Reviews WordCloud")

    if negative_text.strip():
        neg_wc = WordCloud(width=600, height=400, background_color="white").generate(negative_text)
        fig2, ax2 = plt.subplots(figsize=(6,4))
        ax2.imshow(neg_wc, interpolation='bilinear')
        ax2.axis("off")
        st.pyplot(fig2)
    else:
        st.warning("No negative reviews found.")
