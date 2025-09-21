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

#Insert new data in database only in  EmployeeNumber, Department, MonthlyIncome
def add_employee(employee_id, department, new_role, income):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO employees (EmployeeNumber, Department,JobRole, MonthlyIncome) VALUES (?, ?, ?, ?)",
              (employee_id, department,new_role, income))
    conn.commit()
    conn.close() 

#Chack the data inserted if exist by ID Employee 
def employee_exists(employee_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT EmployeeNumber FROM employees WHERE EmployeeNumber = ?", (employee_id,))
    exists = c.fetchone() is not None
    conn.close() 
    return exists

#Get function for the department to add it for add employee function
def get_departments():
    with sqlite3.connect('mydb.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT Department FROM employees")
        rows = cursor.fetchall()
    return [row[0] for row in rows]

#Get function for the Job Role to add it for add employee function

def get_job_roles():
    with sqlite3.connect('mydb.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT JobRole FROM employees")
        rows = cursor.fetchall()
    return [row[0] for row in rows]

#Function count all id in database and +1 to add it to database 
def next_employee_id():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT MAX(EmployeeNumber) FROM employees")
    max_id = c.fetchone()[0]
    conn.close()
    
    if max_id is None:
        return 1
    else:
        return max_id + 1
    

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

    # return to Tab bar (Tab Bar to swap between functions)
    with Tab_Add:
        #form to add the element in it 
        with st.form("add_employee_form"):
            #the header for the form
            st.header("Add a New Employee")
            #take the next number of employee not in database 
            next_id = next_employee_id()
            #add new Employee number 
            new_employee_ID = st.number_input("Employee Number", min_value=1, value=next_id, format="%d")
            #take the data from the function
            Department = get_departments
            #select box 
            new_dept = st.selectbox("Departments", options= get_departments(), key="Department")
            #take the data from the function
            Jobrole = get_job_roles
            #select box
            new_role = st.selectbox("Job Role", options= get_job_roles(), key="Job Role select")
            #Input to take the number of income add to Employee
            new_income = st.number_input("Monthly Income", min_value=0, step=1000, format="%d")
            submitted = st.form_submit_button("Add Employee")

            #If statment to check the Employee is exist or not
            if submitted:
                if employee_exists(new_employee_ID):
                    st.error("This Employee ID already exists. Please use a unique ID.")
                elif not new_dept or not new_role or not new_employee_ID or not new_income:
                    st.warning("Please fill in all the details.")
                else:
                    add_employee(new_employee_ID, new_dept, new_role, new_income)
                    st.success("Successfully added employee to the database!")
                    st.session_state['df'] = load_employees() 
                    st.rerun()


