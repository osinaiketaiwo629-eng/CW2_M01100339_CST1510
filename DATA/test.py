import sqlite3
import os

db_path = "DATA/telligence_platform.db"
print("Looking for:", os.path.abspath(db_path))

try:
    conn = sqlite3.connect(db_path)
    print("Connected successfully.")
    conn.close()
except Exception as e:
    print( "Error:", e)
