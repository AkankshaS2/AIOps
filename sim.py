import pandas as pd
import matplotlib.pyplot as plt

# Sample log dataset
data = {
    "Timestamp": [
        "10:00", "10:01", "10:02", "10:03", "10:04",
        "10:05", "10:06", "10:07", "10:08", "10:09",
        "10:10", "10:11", "10:12", "10:13", "10:14",
        "10:15", "10:16", "10:17", "10:18", "10:19"
    ],
    "CPU": [
        45, 52, 48, 55, 60,
        95, 50, 47, 53, 58,
        62, 55, 97, 51, 49,
        57, 60, 54, 92, 56
    ],
    "Memory": [
        50, 52, 51, 53, 54,
        55, 52, 51, 54, 53,
        55, 54, 56, 52, 51,
        53, 55, 54, 52, 53
    ],
    "Response_Time": [
        120, 125, 118, 130, 128,
        135, 122, 119, 125, 127,
        132, 129, 140, 121, 118,
        126, 130, 124, 138, 125
    ]
}

df = pd.DataFrame(data)

# --------------------------------------------------
# 1. Basic statistics
# --------------------------------------------------

print("Total records:", len(df))

print("\nBasic Statistics:")
print(df[["CPU", "Memory", "Response_Time"]].describe())

# --------------------------------------------------
# 2. Threshold-based anomaly detection
# --------------------------------------------------

# CPU greater than 90% is considered anomalous
CPU_THRESHOLD = 90

df["Status"] = df["CPU"].apply(
    lambda x: "ANOMALY" if x > CPU_THRESHOLD else "NORMAL"
)

# Get anomalous records
anomalies = df[df["Status"] == "ANOMALY"]

print("\nAnomalies detected:", len(anomalies))

print("\nAnomalous Records:")
print(anomalies[["Timestamp", "CPU", "Status"]].to_string(index=False))

# --------------------------------------------------
# 3. Display graph
# --------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(df["Timestamp"], df["CPU"], marker="o", label="CPU Usage")

# Highlight anomalies
plt.scatter(
    anomalies["Timestamp"],
    anomalies["CPU"],
    marker="x",
    s=100,
    label="Anomaly"
)

plt.axhline(
    CPU_THRESHOLD,
    linestyle="--",
    label="Threshold (90%)"
)

plt.xlabel("Timestamp")
plt.ylabel("CPU Usage (%)")
plt.title("AIOps CPU Log Anomaly Detection")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.show()