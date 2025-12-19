import streamlit as st
from app.datasets import get_all_datasets_metadata
from app.db import get_db_connection

conn = get_db_connection()
df = get_all_datasets_metadata(conn)    


st.set_page_config(layout="wide")
st.title("Dashboard")

if not st.session_state.get('logged_in', False):
    st.warning("Please log in to access the dashboard.")
    st.stop()


with st.sidebar:
    upload_ = st.selectbox("Uploaded by", df['uploaded_by'].unique())


filtered_df = df[df['uploaded_by'] == upload_]

col1, col2 = st.columns(2)

with col1:

    st.subheader("1st chart")
    st.bar_chart(x = "name", y = "dataset_id", data = filtered_df)

with col2:
    st.subheader("2nd chart")
    st.line_chart(x = "uploaded_by", y = "columns", data = filtered_df)

st.dataframe(filtered_df)
