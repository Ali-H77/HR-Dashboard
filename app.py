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

#Tab Bar to swap between functions
Tab_Dashboard, Tab_Add, Tab_Update = st.tabs(["HR Dashboard","Add New Employee","Update state of Employee"])

# return to Tab bar (Tab Bar to swap between functions)
with Tab_Dashboard:
        #Department filter simple filter the analysis in fig basis on the Department
    department_filter = st.selectbox("Filter by Department:", options=["All"] + sorted(df["Department"].unique().tolist()))
    filtered_df = df if department_filter == "All" else df[df["Department"] == department_filter]

    
