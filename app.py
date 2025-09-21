import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("HR Dashboard program")

#connect SQL to program
def get_connection():
    return sqlite3.connect("mydb.db")

#Load data to program
def load_employees():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM Employees", conn)
    return df

#function to load data to return 
df = load_employees()