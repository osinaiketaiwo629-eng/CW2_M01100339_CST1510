import bcrypt
import sqlite3

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
    user_name = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hash_password(password)
    with open('users.txt', 'a') as f:
        f.write(f"{user_name},{hashed_password}\n")
    print("User registered successfully.")

def login_user(username, password):
    with open('users.txt', 'r') as f:
        for line in f:
            stored_username, stored_hashed = line.strip().split(',')
            if stored_username == username:
                if check_password(password, stored_hashed):
                    print("Login successful.")
                    return True
                else:
                    print("Incorrect password.")
                    return False
        print("Username not found.")
        return False 

#====================================================

conn = sqlite3.connect('DATA/telligence_platform.db')
def add_user(conn, name, hash_password):
    curr = conn.cursor()
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    params = (name, hash_password)
    curr.execute(sql, params)
    conn.commit()

def migrate_users():
    with open('DATA/users.txt', 'r') as f:
        users = f.readlines()
    for user in users:
        name, hash_pw = user.strip().split(',')
        add_user(name, hash_pw)

def get_all_users(conn):
    curr = conn.cursor()
    sql = "SELECT * FROM users"
    curr.execute(sql)
    users = curr.fetchall()
    return users

def get_user(conn, username):
    curr = conn.cursor()
    sql = "SELECT * FROM users WHERE username = ?"
    parram - (username,)
    curr.execute(sql, parram)
    user = curr.fetchone()
    conn.close()
    return user


#===========================================
    

