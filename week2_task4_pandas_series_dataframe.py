# Task 4: Pandas Series and DataFrame
import pandas as pd

marks_series = pd.Series([88, 92, 75, 84, 79], name="Marks")
print("Pandas Series:")
print(marks_series)

data = {
    "Name": ["Katragadda Renusri Lalitha", "Ananya", "Rahul", "Sneha", "Arjun"],
    "Age": [21, 20, 22, 21, 23],
    "Branch": ["CSE Data Science", "CSE", "IT", "CSE Data Science", "ECE"],
    "Marks": [88, 92, 75, 84, 79]
}

df = pd.DataFrame(data)
print("\nStudent DataFrame:")
print(df)

print("\nColumn Names:", df.columns.tolist())
print("Index:", df.index.tolist())

df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 60 else "Fail")
print("\nUpdated DataFrame:")
print(df)
