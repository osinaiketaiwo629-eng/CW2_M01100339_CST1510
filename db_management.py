import sqlite3
import bcrypt

DB_PATH = "DATA/telligence_platform.db"

def create_user_table(conn):
    curr = conn.cursor()
    sql = """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL
    )"""
    curr.execute(sql)
    conn.commit()

def hash_password(pwd):
    password_bytes = pwd.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')

def check_password(pwd, hashed):
    password_bytes = pwd.encode('utf-8')
    hashed_bytes = hashed.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hash_password(password)

    conn = sqlite3.connect(DB_PATH)
    curr = conn.cursor()
    try:
        curr.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    finally:
        conn.close()

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    conn = sqlite3.connect(DB_PATH)
    curr = conn.cursor()
    curr.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    row = curr.fetchone()
    conn.close()

    if row:
        stored_hashed = row[0]
        if check_password(password, stored_hashed):
            print("Login successful.")
            return True
        else:
            print("Incorrect password.")
            return False
    else:
        print("Username not found.")
        return False

def main():
    # Ensure table exists before using
    conn = sqlite3.connect(DB_PATH)
    create_user_table(conn)
    conn.close()

    while True:
        print("\nChoose an option:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()