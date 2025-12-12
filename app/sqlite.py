import sqlite3
def create_users_table():
    conn = sqlite3.connect('DATA/telligence_platform.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE 
                IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn = sqlite3.connect('DATA/telligence_platform.db') 
    conn.commit()
    conn.close()