import psycopg2
import pandas as pd

# Database connection parameters
DB_NAME = "Border_Entry_DB"
DB_USER = "postgres"
DB_PASSWORD = "1710"
DB_HOST = "localhost"
DB_PORT = "1710"

# Establish connection
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

# Define your SQL query
query = "select * from entry_data"

# Load data into a Pandas DataFrame
df = pd.read_sql(query, conn)

# Close the connection
# conn.close()

# Display the first few rows
print(df.head().to_string())

# df.info()

print("Total number of rows in the dataset:", len(df))