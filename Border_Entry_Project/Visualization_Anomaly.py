import matplotlib
matplotlib.use('TkAgg')  # Ensures compatibility with PyCharm GUI
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
from Anomally_1 import df  # Ensure this contains all columns used below

# --------- VISUALIZATION 3: Anomaly Count by Season ----------
print("📊 Plotting Anomaly Count by Season...")

anomaly_counts = df.groupby('season')['anomaly'].apply(lambda x: (x == 'anomaly').sum()).reindex(["Spring", "Summer", "Fall", "Winter"]).reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(
    data=anomaly_counts,
    x='season',
    y='anomaly',
    hue='season',
    palette='Set2',
    legend=False
)
print("Total number of rows in the dataset:", len(df))

plt.title("Anomaly Count by Season")
plt.ylabel("Number of Anomalies")
plt.xlabel("Season")
plt.tight_layout()
plt.show()

print("✅ Done: Anomaly Count Plot\n")