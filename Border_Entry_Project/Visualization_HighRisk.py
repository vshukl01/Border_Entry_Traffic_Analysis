import matplotlib
matplotlib.use('TkAgg')  # Ensures compatibility with PyCharm GUI
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
from High_risk_prediction import df

# --------- VISUALIZATION 2: High-Risk % by Season ----------
print("📊 Plotting Proportion of High-Risk Predictions by Season...")

season_risk = df.groupby('season')['risk_prediction'].mean().reindex(["Spring", "Summer", "Fall", "Winter"]).reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(
    data=season_risk,
    x='season',
    y='risk_prediction',
    hue='season',
    palette='flare',
    legend=False
)
print("Total number of rows in the dataset:", len(df))

plt.title("Proportion of High-Risk Predictions by Season")
plt.ylabel("High Risk Probability")
plt.xlabel("Season")
plt.tight_layout()
plt.show()

print("✅ Done: High-Risk Percentage Plot\n")
