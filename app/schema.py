import sqlite3
import pandas as pd

DB_PATH = 'DATA/telligence_PLatform.db'

def create_user_table(conn):
    curr = conn.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    """
    curr.execute(sql)
    conn.commit()
def load_datasets_metadata(conn):
    datasets_metadata = pd.read_csv('DATA/datasets_metadata.csv')
    datasets_metadata.to_sql('datasets_metadata', conn, if_exists='replace', index=False)

if __name__ == "__main__":
     conn = sqlite3.connect(DB_PATH)
     create_user_table(conn)
     load_datasets_metadata(conn)
     conn.close()
     print("User table created successfully.")



