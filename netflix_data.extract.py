import pandas as pd
from sqlalchemy import create_engine

# Load the CSV file
df = pd.read_csv('netflix_titles.csv')

# Create SQLite database named netflix.db (or connect if it already exists)
engine = create_engine('sqlite:///netflix.db')
conn = engine.connect()

# Write data to a table called 'netflix_raw'
df.to_sql('netflix_raw', con=conn, index=False, if_exists='replace')

# Close connection
conn.close()

# Optional: Data checks
print(df.head())
print(df[df.show_id == 's5023'])
print("Max description length:", max(df.description.dropna().str.len()))
print("Missing values per column:\n", df.isna().sum())
