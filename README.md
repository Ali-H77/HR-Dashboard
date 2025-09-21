# 📊 HR Dashboard
A Streamlit-based web application to manage and visualize employee data using an SQLite database. This tool helps HR professionals make data-driven decisions and streamline employee record management.

## 📚 Table of Contents

- [📊 Featuers]
- [📈 Visual Demo]
- [📌 Project Overview]
- [🗂️ Data Source ]
- [🛠️ Technology Stack]
- [🚀 Setup and Local Installation]
- [📄 License]

## Features:

📈 View insightful employee analytics and dashboards
Visualize data like department-wise distribution, gender ratio, salary trends, and more.

➕ Add new employee records
Easily input and store new employee data via interactive forms.

✏️ Update existing employee income details
Modify salary or compensation information for existing employees with ease.

## 📌 Project Overview
This HR Dashboard application enables HR professionals to:
- View insightful analytics including department distribution, salary trends, and gender balance.
- Add and update employee records with ease.
- Store and retrieve data using a lightweight SQLite database.

### 📈 Visual Demo
![
    frist thing appear when open the web page
](<images/Screenshot 2025-09-21 124426.png>)
![
    One of the fig in page
](<images/Screenshot 2025-09-21 124732.png>)
![
    Add New Employee
](<images/Screenshot 2025-09-21 124842.png>)
![
    Update Income for Employee
](<images/Screenshot 2025-09-21 124951.png>)

### 🎯 Purpose & Value

Manual HR record keeping can be inefficient and error-prone. This dashboard simplifies:
- Real-time employee data management.
- Interactive visual reporting.
- Efficient onboarding and salary adjustment.


---

## 🗂️ Data Source 
 
 ### 📥 Data Source
The sample data was sourced from [Kaggle – HR Dataset](https://www.kaggle.com/datasets) or manually created for simulation purposes.
 ### Data Dictionary
 - Age: Employee's age in years
 - Attrition: Whether the employee has left the company (Yes/No)
 - BusinessTravel: Frequency of business travel (e.g., Rarely, Frequently, Non-Travel)
 - DailyRate: Daily pay rate of the employee
 - Department: The department the employee belongs to (e.g., Sales, R&D, HR)
 - DistanceFromHome: Distance in kilometers from home to work
 - Education: Education level (1 = Below College, 2 = College, 3 = Bachelor, 4 = Master, 5 = Doctor)
 - EducationField: Field of education (e.g., Life Sciences, Medical, Marketing)
 - EmployeeCount: Number of employees (usually 1 for individual entries)
 - EmployeeNumber: Unique employee identifier
 - EnvironmentSatisfaction: Satisfaction rating with work environment (1 = Low to 4 = Very High)
 - Gender: Employee's gender (Male/Female)
 - HourlyRate: Hourly pay rate
 - JobInvolvement: Level of job involvement (1 = Low to 4 = High)
 - JobLevel: Hierarchical job level (1 = Entry to 5 = Executive)
 - JobRole: Specific role or title of the employee
 - JobSatisfaction: Job satisfaction rating (1 = Low to 4 = Very High)
 - MaritalStatus: Marital status of the employee (Single, Married, Divorced)
 - MonthlyIncome: Monthly income in SAR
 - MonthlyRate: Monthly pay rate
 - NumCompaniesWorked: Number of previous employers
 - Over18: Whether the employee is over 18 years old (Yes)
 - OverTime: Whether the employee works overtime (Yes/No)
 - PercentSalaryHike: Percentage increase in salary over last hike
 - PerformanceRating: Performance rating (1 = Low to 4 = Outstanding)
 - RelationshipSatisfaction: Satisfaction with relationships at work (1 = Low to 4 = Very High)
 - StandardHours: Standard working hours per week (usually 80)
 - StockOptionLevel: Stock option level granted (0 = None to 3 = High)
 - TotalWorkingYears: Total years of professional experience
 - TrainingTimesLastYear: Number of training sessions attended last year
 - WorkLifeBalance: Work-life balance rating (1 = Bad to 4 = Best)
 - YearsAtCompany: Number of years with the current company
 - YearsInCurrentRole: Number of years in the current role
 - YearsSinceLastPromotion: Years since the last promotion
 - YearsWithCurrManager: Years working with the current manager

## 🛠️ Technology Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **Backend**: Python 3.10
- **Database**: SQLite
- **Data Analysis & Handling**: pandas, numpy
- **Visualization**: matplotlib, seaborn, plotly (optional)

## 🚀 Setup and Local Installation
- Install all packages required

```
pip install -r requirements.txt
```

- Run the Streamlit app

```
streamlit run app.py
```


---

## 📄 License

- This project is licensed under the MIT License.

## Author 
Ali H Alhussain