from Connector_df import df  # Your original DataFrame
import pandas as pd

# ------------------ TRAFFIC NORMALIZATION ------------------
df['traffic_density'] = df.groupby(['year', 'month', 'state'])['value'].transform('sum')

state_populations = {
    'TX': 29527941, 'CA': 39538223, 'AZ': 7151502, 'NY': 20201249,
    'MI': 10077331, 'MN': 5706494, 'WA': 7693612, 'ND': 779094,
    'ME': 1362359, 'ID': 1839106, 'MT': 1084225, 'AK': 733391,
    'NM': 2117522, 'VT': 643077
}
pop_df = pd.DataFrame(state_populations.items(), columns=['state', 'population'])
df = df.merge(pop_df, on='state', how='left')

df['traffic_per_capita'] = df['traffic_density'] / df['population']
monthly_stats = df.groupby(['year', 'month'])['traffic_density'].agg(['mean', 'std']).reset_index()
df = df.merge(monthly_stats, on=['year', 'month'], how='left')
df['traffic_z_score'] = (df['traffic_density'] - df['mean']) / df['std']

print("\n SECTION 1 COMPLETE: Traffic Normalization")
print(df[['state', 'year', 'month', 'traffic_density', 'traffic_per_capita', 'traffic_z_score']].head())

print(df.head().to_string())

print("Total number of rows in the dataset:", len(df))

