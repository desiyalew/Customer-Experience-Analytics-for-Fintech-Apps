import oracledb
import pandas as pd
import os

# Connect to Oracle XE
conn = oracledb.connect(
    user='YeabDev',
    password='admin',
    dsn='localhost/orcl'
)

cursor = conn.cursor()

# Load CSV
df = pd.read_csv('../data/thematic_reviews/thematic_reviews.csv')

# Map bank names to IDs
bank_map = {
    'CBE': 1,
    'BOA': 2,
    'Dashen': 3
}

# Insert reviews
print("Inserting reviews...")
for _, row in df.iterrows():
    try:
        cursor.execute("""
            INSERT INTO reviews (
                review_id, bank_id, rating, review_text,
                sentiment_label, sentiment_score, review_date, theme
            ) VALUES (:1, :2, :3, :4, :5, :6, :7, :8)
        """, [
            row.name + 1,               # review_id (simple index-based ID)
            bank_map[row['bank']],      # bank_id from mapping
            int(row['rating']),
            str(row['review'])[:4000],  # Truncate long texts if necessary
            str(row['sentiment_label']),
            float(row['sentiment_score']),
            pd.to_datetime(row['date']),
            str(row['theme'])
        ])
    except Exception as e:
        print(f"Error inserting row {row.name}: {e}")

# Commit and close
conn.commit()
cursor.close()
conn.close()
print("✅ Data successfully inserted into Oracle.")