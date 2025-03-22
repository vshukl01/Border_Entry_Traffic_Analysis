import pandas as pd
from Analysis_top_ports import future_df, top_ports
from Connector_df import df

# ------------------ 1. Export CSV Files ------------------
future_df.to_csv("forecasted_ports.csv", index=False)
print("------------------------------------------------------------")
print("✓ Saved: forecasted_ports.csv")

# Recompute busiest months
monthly_totals = df[df['port_name'].isin(top_ports)].groupby(['port_name', 'year', 'month'])['value'].sum().reset_index()
monthly_totals['rank'] = monthly_totals.groupby(['port_name', 'year'])['value'].rank(ascending=False, method='min')
busiest_months = monthly_totals[monthly_totals['rank'] == 1]
busiest_months.to_csv("busiest_months.csv", index=False)
print("✓ Saved: busiest_months.csv")

# Top 10 Transport Modes
top_ports_df = df[df['port_name'].isin(top_ports)]
top_transport_modes = (
    top_ports_df.groupby('measure')['value']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
top_transport_modes.to_csv("transport_modes.csv", index=False)
print("✓ Saved: transport_modes.csv")
print("------------------------------------------------------------")

# ------------------ 2. Wrap-Up Report Content ------------------

wrapup_lines = []
wrapup_lines.append("==========================================================================")
wrapup_lines.append("                      BORDER ENTRY FORECASTING REPORT                     ")
wrapup_lines.append("==========================================================================")
wrapup_lines.append("All forecasting and analysis steps have been successfully completed.")
wrapup_lines.append("This report summarizes key findings based on historical and forecasted data.\n")

total_ports = future_df['port_name'].nunique()
total_records = len(future_df)
start_year = future_df['year'].min()
end_year = future_df['year'].max()

wrapup_lines.append("Forecasting Summary")
wrapup_lines.append("--------------------------------------------------------------------------")
wrapup_lines.append(f"Total forecasted records     : {total_records}")
wrapup_lines.append(f"Unique ports forecasted      : {total_ports}")
wrapup_lines.append(f"Forecasting time period      : {start_year} through {end_year}\n")

# Top 10 ports
wrapup_lines.append("Top 10 Ports by Total Forecasted Border Entry Volume")
wrapup_lines.append("--------------------------------------------------------------------------")
wrapup_lines.append("Rank | Port Name                    | Predicted Total Entries")
wrapup_lines.append("-----|------------------------------|--------------------------")

top_10_ports = (
    future_df.groupby('port_name')['predicted_value']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

for idx, row in top_10_ports.head(10).iterrows():
    wrapup_lines.append(f"{idx + 1:>4} | {row['port_name']:<28} | {row['predicted_value']:>20,}")

wrapup_lines.append("\nExplanation")
wrapup_lines.append("--------------------------------------------------------------------------")
wrapup_lines.append("The rankings above represent the ports expected to experience the highest")
wrapup_lines.append("total volume of inbound traffic over the forecast period.")
wrapup_lines.append("These values are based on historical trends modeled using linear regression,")
wrapup_lines.append("projected forward from the most recent available year in the dataset.")
wrapup_lines.append(f"Each value reflects the sum of all predicted yearly entries for that port")
wrapup_lines.append(f"between {start_year} and {end_year}.\n")

wrapup_lines.append("==========================================================================")

# ------------------ 3. Write to File & Print ------------------

# Save to text file
with open("forecasting_summary_report.txt", "w") as f:
    f.write("\n".join(wrapup_lines))

# Also print to terminal
print("\n".join(wrapup_lines))
print("✓ Saved: forecasting_summary_report.txt")
