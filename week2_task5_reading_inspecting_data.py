# Task 5: Reading and Inspecting Data
import pandas as pd

data = """StudentID,Name,Branch,Marks,Attendance
101,Katragadda Renusri Lalitha,CSE Data Science,88,92
102,Ananya,CSE,92,95
103,Rahul,IT,75,80
104,Sneha,CSE Data Science,84,88
105,Arjun,ECE,79,85
106,Priya,CSE,91,94
107,Kiran,IT,68,72
108,Meena,ECE,83,90"""

with open("students.csv", "w") as file:
    file.write(data)

df = pd.read_csv("students.csv")

print("First 5 Rows:")
print(df.head())
print("\nLast 5 Rows:")
print(df.tail())
print("\nNumber of Rows and Columns:", df.shape)
print("Column Names:", df.columns.tolist())
print("\nData Types:")
print(df.dtypes)
print("\nDataset Information:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())
