import streamlit as st
from app.db import get_db_connection
from app.users import hash_password, add_user
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
        st.session_state['logged_in'] = True
        st.success("You are now logged in.")

with tab_register: 
    st.info ("Registration:")
    reg_name = st.text_input("New Username:") 
    reg_password = st.text_input("Choose a new Password:", type="password")
    if st.button("Register"):
        hashed_psw = hash_password(reg_password)
        add_user (conn, reg_name, hashed_psw)
        st.success("You have registered successfully. Please log in.")
