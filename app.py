# app.py

import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(page_title="🎶 Music Genre Classifier", layout="centered")

# Title
st.title("🎼 AI Music Genre Classifier")
st.markdown("Upload your feature file or try a test sample to predict the music genre.")

# Load the trained model
model = joblib.load("music_genre_classifier.pkl")

# Option 1: Upload CSV
uploaded_file = st.file_uploader("📂 Upload a CSV file with extracted features", type=["csv"])

# Option 2: Try a preloaded test sample
if not uploaded_file:
    st.info("Or try one of the sample test inputs below:")
    sample_df = pd.read_csv("test_samples.csv")
    sample_index = st.slider("Select Sample Number", 0, len(sample_df) - 1, 0)
    data = sample_df.iloc[[sample_index]]
else:
    data = pd.read_csv(uploaded_file)

# Show input data
st.subheader("📊 Input Features")
st.dataframe(data)

# Predict
if st.button("🎯 Predict Genre"):
    prediction = model.predict(data)
    st.success(f"🎵 Predicted Genre: **{prediction[0]}**")
