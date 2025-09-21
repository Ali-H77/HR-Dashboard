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

    #Fig Bar include : (X = Department , Y = MonthlyIncome)
    fig_bar = px.bar(filtered_df, x="Department", y="MonthlyIncome", color="Department", title="Employee Income by Department")
    st.plotly_chart(fig_bar)

    #Fig Pie
    fig_pie = px.pie(df, names="Department", title="Employee Count by Department")
    st.plotly_chart(fig_pie)

    #Fig Histogram with Education and color by Department
    fig_H2 = px.histogram(df, y="Education", color="Department", barmode="group",title="Percentage of Education Levels by Department")
    st.plotly_chart(fig_H2)

    #Fig Histogram with Gender and color by Department
    fig_histogram = px.histogram(df,x="Gender", color="Department", barmode="group", title="Gender by Department")
    st.plotly_chart(fig_histogram)
    
    #table of the all data in database
    st.subheader("Employee Table")
    st.dataframe(filtered_df)

