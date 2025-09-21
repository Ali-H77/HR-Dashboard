# ===================================================
# === Import Libraries ===
# ===================================================
import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
from PIL import Image

#add image in streamlit
logo = Image.open('images/Solutions logo.png')
st.image(logo,width= 200)


st.title("HR Dashboard program")

#connect SQL to program
def get_connection():
    return sqlite3.connect("data/mydb.db")

# ===================================================
# === Data Loading ===
# ===================================================

def load_employees():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM Employees", conn)
    return df

# ===================================================
# === Data Processing ===
# ===================================================

def add_employee(employee_id, department, new_role, income):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO employees (EmployeeNumber, Department,JobRole, MonthlyIncome) VALUES (?, ?, ?, ?)",
              (employee_id, department,new_role, income))
    conn.commit()
    conn.close() 

# ===================================================
# === Data Processing ===
# ===================================================

def employee_exists(employee_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT EmployeeNumber FROM employees WHERE EmployeeNumber = ?", (employee_id,))
    exists = c.fetchone() is not None
    conn.close() 
    return exists

# ===================================================
# === Data Processing ===
# ===================================================
def update_employee(emp_id, income):
    try:
        with sqlite3.connect('mydb.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE employees SET MonthlyIncome = ? WHERE EmployeeNumber = ?", 
                (float(income), int(emp_id))
            )
            conn.commit()
            if cursor.rowcount == 0:
                return False, "No employee found with that ID"
            return True, "Update successful"
    except Exception as e:
        return False, str(e)

# ===================================================
# === Data Loading ===
# ===================================================

def get_departments():
    with sqlite3.connect('data/mydb.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT Department FROM employees")
        rows = cursor.fetchall()
    return [row[0] for row in rows]

# ===================================================
# === Data Loading ===
# ===================================================
def get_job_roles():
    with sqlite3.connect('data/mydb.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT JobRole FROM employees")
        rows = cursor.fetchall()
    return [row[0] for row in rows]

# ===================================================
# === Data Processing ===
# ===================================================
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


# ===================================================
# === Main Program ===
# ===================================================

#Tab Bar to swap between functions
Tab_Dashboard, Tab_Add, Tab_Update = st.tabs(["HR Dashboard","Add New Employee","Update state of Employee"])

# return to Tab bar (Tab Bar to swap between functions)
with Tab_Dashboard:
        #Department filter simple filter the analysis in fig basis on the Department
    department_filter = st.selectbox("", options=["All"] + sorted(df["Department"].unique().tolist()))
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
            st.title("Add a New Employee")
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


    # return to Tab bar (Tab Bar to swap between functions)
    with Tab_Update:
        st.title("Update Employee Monthly Income")
        #Input for Employee ID and New Income
        emp_id = st.text_input("Employee ID")
        income = st.text_input("New Monthly Income")
        #If Statment check if Emplyee is exist from Employee ID
        if st.button("Check Employee Exists"):
            if emp_id.isdigit():
                if employee_exists(emp_id):
                    st.success(f"Employee {emp_id} found!")
                else:
                    st.error(f"Employee {emp_id} not found.")
            else:
                st.error("Employee ID must be a number.")
            #update the income of employee 
        if st.button("Update Income"):
            if not emp_id.isdigit():
                st.error("Employee ID must be a number")
            else:
                try:
                    float(income)
                    success, msg = update_employee(emp_id, income)
                    if success:
                        st.success(msg)
                    else:
                        st.error(msg)
                except ValueError:
                    st.error("Monthly Income must be a number")


st.markdown("""
    <style>
      .stApp {
        background-color: #800080;
        }

        /* Style Streamlit titles (optional) */
        h1, h2, h3, h4 {
            color: white !important;
        }

        /* Force all buttons to have white background and black text */
        div.stButton > button {
            background-color: white !important;
            color: black !important;
            font-weight: bold;
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 0.5em 1em;
            width: 100%;
            margin-bottom: 10px;
        }

        /* Button hover effect */
        div.stButton > button:hover {
            background-color: #f2f2f2 !important;
            color: black !important;
        }
        .stTabs [role="tab"] {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)