import streamlit as st
from app.db import get_db_connection
from app.users import hash_password, add_user, login_user
conn = get_db_connection()
st.set_page_config(layout="wide")


st.header("Home")
st.write("Welcome to the Home Page. Please log in or register to continue.")    




if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

tab_login,tab_register = st.tabs(["Login", "Register"])

with tab_login:
    login_name = st.text_input("Username:")
    login_password = st.text_input("Password:", type="password")

    if st.button("Log in"):
        if login_user(conn, login_name, login_password):
            st.session_state['logged_in'] = True
            st.session_state['username'] = login_name.strip()
            st.success("Login successful!")
        else:
            st.session_state['logged_in'] = False
            st.error("Invalid username or password.")
            
with tab_register: 
    st.info ("Registration:")
    reg_name = st.text_input("New Username:") 
    reg_password = st.text_input("Choose a new Password:", type="password")
    if st.button("Register"):
        if not reg_name.strip() or not reg_password.strip():
            st.error("Username and password cannot be empty.")
        elif len(reg_password) < 8:
            st.error("Password must be at least 8 characters long.")
        elif add_user(conn, reg_name, hash_password(reg_password)):
            st.success("User registered successfully!")
        else:
            st.error("User already exists. Please choose a different username.")    