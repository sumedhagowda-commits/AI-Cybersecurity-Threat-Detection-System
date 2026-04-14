from src.data_loader import load_data
from src.preprocess import preprocess
from src.model import train_model
from src.detect import detect
import matplotlib.pyplot as plt
import numpy as np

print("🚀 SYSTEM STARTED")

# Step 1: Load data
df = load_data("data/kddcup.csv")
print("✅ Dataset Loaded")

# Step 2: Preprocess
df = preprocess(df)

# Keep only numeric features
X = df.select_dtypes(include=['int64', 'float64'])

print("🧠 Training Model...")

# Step 3: Train model
model = train_model(X)

# Step 4: Detect anomalies
predictions = detect(model, X)

print("🔍 Detection Completed")

# Step 5: Convert predictions
normal = np.sum(predictions == 1)
anomaly = np.sum(predictions == -1)

print("\n📊 RESULTS")
print("Normal Traffic:", normal)
print("Anomalies Detected:", anomaly)

# Step 6: ALERT SYSTEM
if anomaly > 0:
    print("\n🚨 ALERT: Suspicious activity detected!")
else:
    print("\n✅ System is safe")

# Step 7: Visualization
labels = ['Normal', 'Anomaly']
values = [normal, anomaly]

plt.bar(labels, values)
plt.title("Cybersecurity Threat Detection")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

print("\n🏁 Threat Detection Completed Successfully")