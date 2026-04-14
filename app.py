import streamlit as st
import numpy as np
from src.data_loader import load_data
from src.preprocess import preprocess
from src.model import train_model
from src.detect import detect
import matplotlib.pyplot as plt

st.title("🛡 AI Cybersecurity Threat Detection System")

# Step 1: Load data
st.write("📂 Loading dataset...")
df = load_data("data/kddcup.csv")
st.success("Dataset Loaded")

# Step 2: Preprocess
df = preprocess(df)
X = df.select_dtypes(include=['int64', 'float64'])

# Step 3: TRAIN BUTTON (IMPORTANT FIX)
if st.button("🚀 Train Model & Detect Threats"):

    st.info("🧠 Training model... Please wait")

    model = train_model(X)

    st.success("Model Trained Successfully")

    # Step 4: Prediction
    predictions = detect(model, X)

    normal = np.sum(predictions == 1)
    anomaly = np.sum(predictions == -1)

    st.write("## 📊 Results")
    st.write("Normal Traffic:", normal)
    st.write("Anomalies Detected:", anomaly)

    # Step 5: ALERT
    if anomaly > 0:
        st.error("🚨 ALERT: Suspicious Activity Detected!")
    else:
        st.success("✅ System Safe")

    # Step 6: GRAPH
    fig, ax = plt.subplots()
    ax.bar(["Normal", "Anomaly"], [normal, anomaly])
    ax.set_title("Threat Detection Summary")

    st.pyplot(fig)