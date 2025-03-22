from Analysis_top_ports import top_ports
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns
from Connector_df import df  # Ensure this loads your full cleaned DataFrame

# ------------------ BUSIEST MONTHS FOR TOP PORTS ------------------
print("\nFinding Busiest Months for Top Ports...")

top_ports_df = df[df['port_name'].isin(top_ports)]
monthly_peak = top_ports_df.groupby(['port_name', 'year', 'month'])['value'].sum().reset_index()
monthly_peak['rank'] = monthly_peak.groupby(['port_name', 'year'])['value'].rank(ascending=False, method='min')
busiest_months = monthly_peak[monthly_peak['rank'] == 1]

print(f"Identified busiest months for each year for top {len(top_ports)} ports.")
print("Sample busiest month results:")
print(busiest_months.head())

# Visualization: Busiest Months
plt.figure(figsize=(10, 6))
sns.countplot(data=busiest_months, x='month', hue='port_name')
plt.title("Busiest Months per Port (Top 10 Ports)")
plt.xlabel("Month")
plt.ylabel("Frequency as Busiest Month")
plt.tight_layout()
plt.savefig("Busiest Months per Port (Top 10 Ports).png", dpi=300)
plt.show()



# ------------------ Total Entry Visualization ------------------
# Group by (port_name, year, month) to find total entries
monthly_totals = df[df['port_name'].isin(top_ports)].groupby(['port_name', 'year', 'month'])['value'].sum().reset_index()

# Get the busiest month per year per port
monthly_totals['rank'] = monthly_totals.groupby(['port_name', 'year'])['value'].rank(ascending=False, method='min')
busiest_months = monthly_totals[monthly_totals['rank'] == 1]

# Now group to find total volume per month across ports
month_entry_totals = busiest_months.groupby('month')['value'].sum().reset_index()

# 🔢 Convert month number to label (optional)
month_map = {
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr',
    5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug',
    9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
}
month_entry_totals['month_name'] = month_entry_totals['month'].map(month_map)

# 🖼 Plot: Actual Entry Volumes for Busiest Months
plt.figure(figsize=(12, 6))
ax = sns.barplot(data=month_entry_totals, x='month_name', y='value', palette='viridis')

plt.title("Total Border Entries for Busiest Months (Top 10 Ports)")
plt.xlabel("Month")
plt.ylabel("Total Entry Value (Busiest Months Only)")

# 🧾 Add number labels on top of each bar
for bar in ax.patches:
    height = int(bar.get_height())
    ax.annotate(f'{height:,}', (bar.get_x() + bar.get_width() / 2, height),
                ha='center', va='bottom', fontsize=9, color='black')

plt.tight_layout()
plt.savefig("Total Border Entries for Busiest Months (Top 10 Ports).png", dpi=300)
plt.show()


