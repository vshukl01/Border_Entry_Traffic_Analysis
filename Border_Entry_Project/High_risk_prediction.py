import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from Traffic_Normalization_0 import df


# Convert month abbreviations to numeric values
month_map = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
    'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
    'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}
df['month'] = df['month'].map(month_map)


# ------------------ HIGH-RISK PREDICTION ------------------
df['risk_label'] = np.where(df['traffic_z_score'] >= df['traffic_z_score'].quantile(0.90), 1, 0)
df['state_code'] = df['state'].astype('category').cat.codes
df['season_code'] = df['season'].astype('category').cat.codes

features = ['year', 'month', 'state_code', 'port_code', 'traffic_density',
            'traffic_per_capita', 'traffic_z_score', 'season_code']
X = df[features]
y = df['risk_label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
df['risk_prediction'] = model.predict(X)

print("\n✅ SECTION 2 COMPLETE: High-Risk Prediction")
print(classification_report(y_test, model.predict(X_test)))
print(df[['state', 'year', 'month', 'risk_prediction']].head())

print(df.head().to_string())

print("Total number of rows in the dataset:", len(df))