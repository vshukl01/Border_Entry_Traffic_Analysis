import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from Connector_df import df  # Ensure this loads your full cleaned DataFrame

# ------------------ SETUP ------------------
print("Dataset Loaded from Connector_df")
print(f"Dataset contains {len(df)} rows and {df.shape[1]} columns.")
print("Columns:", list(df.columns))
print("Sample rows:")
print(df.head(3))

# ------------------ CLEANING & TYPE CASTING ------------------
print("\nCasting Columns to Correct Types...")

# Map month names to numbers
month_map = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
    'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
    'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}
df['month'] = df['month'].map(month_map)

# Cast other types
df['year'] = df['year'].astype(int)
df['month'] = df['month'].astype(int)
df['value'] = df['value'].astype(int)
df['port_code'] = df['port_code'].astype(int)

print("Data types converted successfully.")

# ------------------ FORECASTING TOP PORTS ------------------
print("\nForecasting Top Ports for the Next 10 Years (Using Linear Regression)")

# Aggregate yearly traffic by port
port_yearly = df.groupby(['port_name', 'year'])['value'].sum().reset_index()
print(f"Aggregated yearly traffic for {port_yearly['port_name'].nunique()} unique ports.")

# Generate forecast range (e.g., 2026–2036)
future_years = list(range(df['year'].max() + 1, df['year'].max() + 11))
print(f"Forecasting traffic for years: {future_years}")

# Build predictions
future_preds = []
skipped_ports = 0

for port in port_yearly['port_name'].unique():
    port_df = port_yearly[port_yearly['port_name'] == port]
    if len(port_df) < 3:
        skipped_ports += 1
        continue  # skip if not enough data

    X = port_df[['year']]
    y = port_df['value']
    model = LinearRegression()
    model.fit(X, y)

    for year in future_years:
        predicted = predicted = model.predict(pd.DataFrame({'year': [year]}))[0]
        future_preds.append({'port_name': port, 'year': year, 'predicted_value': int(predicted)})

future_df = pd.DataFrame(future_preds)
future_df['rank'] = future_df.groupby('year')['predicted_value'].rank(ascending=False, method='min')

print(f"Forecasting complete for {future_df['port_name'].nunique()} ports.")
print(f"Skipped {skipped_ports} ports due to insufficient data (<3 years).")
print("Sample Forecasted Data:")
print(future_df.head())



# ------------------ VISUALIZATION: Top 10 Ports Forecast ------------------
top_ports = future_df.groupby('port_name')['predicted_value'].sum().nlargest(10).index.tolist()
top_future_df = future_df[future_df['port_name'].isin(top_ports)]

print(f"\nTop 10 Forecasted Ports: {top_ports}")

plt.figure(figsize=(14, 7))
sns.set_palette("tab10")
sns.lineplot(data=top_future_df, x='year', y='predicted_value', hue='port_name', marker='o')
plt.title("Forecasted Border Entries for Top 10 Ports (Next 10 Years)")
plt.ylabel("Predicted Border Entries")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()
plt.savefig("top_ports_forecast.png", dpi=300)
plt.show()



