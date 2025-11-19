import bcrypt 

def hash_password(pwd):
password_bytes = pwd.encode('utf-8')
salt = bcrypt.gensalt() 
hashed = bcrypt.hashpw(password_bytes, salt)
return hashed.decode('utf-8')

def check_password(pwd, hashed):
    password_bytes = pwd.encode('utf-8')
    hashed_bytes = hashed.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_bytes)

def register_user(username, password):
        user_name = input("Enter username: ")
        password = input("Enter password: ")    
        hashed_password = hash_password(password)
        with open('users.txt', 'a') as f:   #
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
                        return False    print("Username not found.")         return False
        
        pass