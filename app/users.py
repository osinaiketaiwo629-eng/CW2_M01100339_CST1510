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
    try:
        return bcrypt.checkpw(password_bytes, hashed_bytes)
    except ValueError:
        return False


#====================================================


def add_user(conn, name, password_hash):
    curr = conn.cursor()
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    name = name.strip() 
    params = (name, password_hash)
    
    try:
        curr.execute(sql, params)
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print(f"User '{name}' already exists.")
        return False
    

def get_all_users(conn):
    curr = conn.cursor()
    sql = "SELECT id, username FROM users"
    curr.execute(sql)
    users = curr.fetchall()
    return users

def get_user(conn, username):
    username = username.strip()
    curr = conn.cursor()
    sql = "SELECT * FROM users WHERE username = ?"
    params = (username,)
    curr.execute(sql, params)
    user = curr.fetchone()
    return user

def login_user(conn, username, password):
    user = get_user(conn, username)
    if user and check_password(password, user[2]):  # Assuming password_hash is at index 2
        return True
    return False