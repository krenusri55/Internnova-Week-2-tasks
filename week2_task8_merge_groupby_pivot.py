# Task 8: Merge, Concatenate, GroupBy and Pivot Table
import pandas as pd

students = pd.DataFrame({
    "StudentID": [101, 102, 103, 104],
    "Name": ["Katragadda Renusri Lalitha", "Ananya", "Rahul", "Sneha"],
    "Branch": ["CSE Data Science", "CSE", "IT", "CSE Data Science"]
})

marks = pd.DataFrame({
    "StudentID": [101, 102, 103, 104],
    "Marks": [88, 92, 75, 84],
    "Attendance": [92, 95, 80, 88]
})

merged = pd.merge(students, marks, on="StudentID")
print("Merged DataFrame:")
print(merged)

new_students = pd.DataFrame({
    "StudentID": [105, 106],
    "Name": ["Arjun", "Priya"],
    "Branch": ["ECE", "CSE"],
    "Marks": [79, 91],
    "Attendance": [85, 94]
})

concatenated = pd.concat([merged, new_students], ignore_index=True)
print("\nConcatenated DataFrame:")
print(concatenated)

grouped = concatenated.groupby("Branch").agg(
    Total_Students=("Name", "count"),
    Average_Marks=("Marks", "mean"),
    Highest_Marks=("Marks", "max"),
    Total_Marks=("Marks", "sum")
)
print("\nGroupBy Analysis by Branch:")
print(grouped)

pivot = pd.pivot_table(
    concatenated,
    values="Marks",
    index="Branch",
    aggfunc=["mean", "max", "count"]
)
print("\nPivot Table:")
print(pivot)
