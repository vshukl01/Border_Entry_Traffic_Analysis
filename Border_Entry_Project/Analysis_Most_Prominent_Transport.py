from Analysis_top_ports import future_df, top_ports
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
from Connector_df import df  # Ensure this loads your full cleaned DataFrame

# ------------------ MOST PROMINENT TRANSPORT MODES (TOP 10 PORTS ONLY) ------------------
print("STEP: Identifying Top 10 Transportation Methods at Top 10 Forecasted Ports...")

# Filter dataset to only Top 10 forecasted ports
top_ports_df = df[df['port_name'].isin(top_ports)]

# Group by transport mode (measure) and sum the values
measure_totals = top_ports_df.groupby('measure')['value'].sum().sort_values(ascending=False).reset_index()

# Get top 10 transportation types
top_transport_modes = measure_totals.head(10)

print("Top 10 Transportation Methods by Total Volume (Top 10 Ports Only):")
print(top_transport_modes)

# Visualization
plt.figure(figsize=(12, 6))
sns.barplot(data=top_transport_modes, x='measure', y='value', palette='muted')
plt.title("Top 10 Transportation Methods into the US (Top 10 Ports Only)")
plt.ylabel("Total Entry Volume")
plt.xlabel("Transport Method")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("Top 10 Transportation Methods at Top 10 Forecasted Ports.png", dpi=300)
plt.show()



