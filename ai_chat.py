import streamlit as st  
from openai import OpenAI 
st.title("Chat with AI")

if "messages" not in st.session_state:  
    st.session_state.messages = []

prompt = st.text_input("What's on your mind?")  
if prompt: 
    st.session_state.messages.append({"role": "user", "content": prompt})   
    st.chat_message('User').markdown(prompt)

    completion = OpenAI.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages


reply = completion.choices[0].message.content
    st.session_state.messages.append({"role": reply.role, "content": reply.content})
    st.chat_message('AI').markdown(reply.content)  )