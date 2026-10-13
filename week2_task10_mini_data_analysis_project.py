# Task 10: Mini Data Analysis Project
import pandas as pd
import numpy as np

data = """StudentID,Name,Branch,Marks,Attendance,StudyHours
101,Katragadda Renusri Lalitha,CSE Data Science,88,92,6
102,Ananya,CSE,92,95,7
103,Rahul,IT,75,80,4
104,Sneha,CSE Data Science,84,88,5
105,Arjun,ECE,79,85,5
106,Priya,CSE,91,94,7
107,Kiran,IT,68,72,3
108,Meena,ECE,83,90,5
109,Ravi,CSE Data Science,NaN,86,5
110,Divya,CSE,87,NaN,6"""

with open("student_performance.csv", "w") as file:
    file.write(data)

df = pd.read_csv("student_performance.csv")

print("First 5 Rows:")
print(df.head())
print("\nDataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

print("\nStudents with Marks above 80:")
high_scorers = df[df["Marks"] > 80]
print(high_scorers[["Name", "Branch", "Marks"]])

print("\nTop Students by Marks:")
print(df.sort_values(by="Marks", ascending=False)[["Name", "Marks"]].head())

branch_analysis = df.groupby("Branch").agg(
    Students=("Name", "count"),
    Average_Marks=("Marks", "mean"),
    Average_Attendance=("Attendance", "mean"),
    Average_StudyHours=("StudyHours", "mean")
)
print("\nBranch-wise Analysis:")
print(branch_analysis)

pivot = pd.pivot_table(df, values="Marks", index="Branch", aggfunc=["mean", "max", "count"])
print("\nPivot Table - Marks by Branch:")
print(pivot)

print("\nKey Insights:")
print("1. Students with higher study hours generally scored higher marks.")
print("2. CSE and CSE Data Science students have comparatively higher average marks.")
print("3. Attendance above 85 is associated with stronger academic performance.")
print("4. The highest marks in the dataset belong to Ananya.")

df.to_csv("cleaned_student_performance.csv", index=False)
print("\nCleaned dataset exported successfully to cleaned_student_performance.csv")
