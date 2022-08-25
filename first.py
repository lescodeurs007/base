import streamlit as st
import pandas as pd
st.title("A Simple Streamlit Web App")
name = st.text_input("Enter your name",' ' )
st.write(f"Hello {name}!")
x = st.slider("Select an integer x", 0, 10, 1)
y = st.slider("Select an integer y", 0, 10, 1)
df = pd.DataFrame({"x": [x], "y": [y] , "x + y": [x + y]}, index = ["addition row"])
st.write(df)

                     
import streamlit as st
import mysql.connector

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

st.write("Connected to:", conn.get_server_info())
cursor=conn.cursor()
a=cursor.execute("Select * from test")
for i in a:
  st.write(i)
