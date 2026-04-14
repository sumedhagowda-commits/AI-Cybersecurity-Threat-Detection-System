# 🛡️ AI-Powered Cybersecurity Threat Detection System

## 📌 Overview

This project is an AI-based cybersecurity system that detects suspicious network activity using machine learning. It simulates real-world Security Operations Center (SOC) monitoring.

---

## 🚨 Problem Statement

Traditional cybersecurity systems rely heavily on manual monitoring, which is slow and inefficient. This project automates threat detection using AI.

---

## 🤖 Solution

A machine learning model (Isolation Forest) is used to:

* analyze network traffic data
* detect anomalies
* generate alerts
* visualize threats

---

## 🧰 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib
* Streamlit

---

## 📊 Dataset

* KDD Cup 1999 Dataset
* Represents simulated network traffic with attack patterns

📥 Download Dataset:
https://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html

Place it in:

```
data/kddcup.csv
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/AI-Cybersecurity-Threat-Detection-System.git
cd AI-Cybersecurity-Threat-Detection-System
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

---

## 🚀 Run Project

### ▶️ Run Python Version

```bash
python main.py
```

### 🌐 Run Dashboard

```bash
python -m streamlit run app.py
```

---

## 📈 Results

* Detection of anomalies in network traffic
* Alert generation for suspicious activity
* Visualization of normal vs attack traffic

---
## 🎯 Features

* Anomaly detection using ML
* SOC-style alert system
* Data visualization
* Streamlit dashboard

---

## 📚 Learning Outcomes

* Machine Learning for Cybersecurity
* Anomaly Detection
* SOC Workflow Simulation
* Data Analysis


