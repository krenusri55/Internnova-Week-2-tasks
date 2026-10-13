# Task 9: Exporting Data
import pandas as pd

data = {
    "Name": ["Katragadda Renusri Lalitha", "Ananya", "Rahul", "Sneha"],
    "Branch": ["CSE Data Science", "CSE", "IT", "CSE Data Science"],
    "Marks": [88, 92, 75, 84],
    "Attendance": [92, 95, 80, 88]
}

df = pd.DataFrame(data)
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 60 else "Fail")

df.to_csv("processed_students.csv", index=False)
print("Data exported successfully to processed_students.csv")

exported_df = pd.read_csv("processed_students.csv")
print("\nContents of Exported CSV File:")
print(exported_df)
