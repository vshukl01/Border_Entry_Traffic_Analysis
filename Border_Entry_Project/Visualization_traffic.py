import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
from Traffic_Normalization_0 import df

# ------------------ SEASONAL VISUALIZATIONS ------------------

# ------------------ VISUALIZATION 1: Average Traffic by Season ------------------
print("📊 Plotting Average Border Traffic Density by Season...")

plt.figure(figsize=(8, 5))
sns.barplot(
    data=df,
    x='season',
    y='traffic_density',
    estimator=np.mean,
    errorbar=None,
    hue='season',
    palette="coolwarm",
    legend=False,
    order=["Spring", "Summer", "Fall", "Winter"]
)
plt.title("Average Border Traffic Density by Season")
plt.ylabel("Avg Traffic Density")
plt.xlabel("Season")
plt.tight_layout()
plt.show()

print("✅ Done: Average Traffic Plot\n")