# Task 6: Selecting, Filtering and Sorting Data
import pandas as pd

data = {
    "Name": ["Katragadda Renusri Lalitha", "Ananya", "Rahul", "Sneha", "Arjun", "Priya"],
    "Branch": ["CSE Data Science", "CSE", "IT", "CSE Data Science", "ECE", "CSE"],
    "Marks": [88, 92, 75, 84, 79, 91],
    "Attendance": [92, 95, 80, 88, 85, 94]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print("\nSelected Columns:")
print(df[["Name", "Marks"]])

print("\nSelected Rows using iloc:")
print(df.iloc[1:4])

print("\nStudents with Marks greater than 80:")
print(df[df["Marks"] > 80])

print("\nCSE Data Science students with Marks greater than 80 and Attendance above 90:")
filtered = df[(df["Branch"] == "CSE Data Science") & (df["Marks"] > 80) & (df["Attendance"] > 90)]
print(filtered)

print("\nSorted by Marks in Ascending Order:")
print(df.sort_values(by="Marks", ascending=True))

print("\nSorted by Marks in Descending Order:")
print(df.sort_values(by="Marks", ascending=False))
