from sklearn.ensemble import IsolationForest
from High_risk_prediction import df
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# ------------------ ANOMALY DETECTION ------------------
iso = IsolationForest(contamination=0.01, random_state=42)
df['anomaly_score'] = iso.fit_predict(df[['value']])
df['anomaly'] = df['anomaly_score'].map({1: 'normal', -1: 'anomaly'})

print("\n✅ SECTION 3 COMPLETE: Anomaly Detection")
print(df[['state', 'month', 'value', 'anomaly']].head())

print(df.head().to_string())

print("Total number of rows in the dataset:", len(df))


