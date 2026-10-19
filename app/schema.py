import sqlite3

DB_PATH = 'DATA/telligence.platform.dbf'

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

if __name__ == "__main__":
     conn = sqlite3.connect(DB_PATH)
     create_user_table(conn)
     conn.close()
     print("User table created successfully.")



