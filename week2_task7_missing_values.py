# Task 7: Handling Missing Values
import pandas as pd
import numpy as np

data = {
    "Name": ["Katragadda Renusri Lalitha", "Ananya", "Rahul", "Sneha", "Arjun"],
    "Age": [21, np.nan, 22, 21, np.nan],
    "Branch": ["CSE Data Science", "CSE", np.nan, "CSE Data Science", "ECE"],
    "Marks": [88, 92, np.nan, 84, 79]
}

df = pd.DataFrame(data)
print("Dataset Before Handling Missing Values:")
print(df)

print("\nMissing Values in Each Column:")
print(df.isnull().sum())

df_removed = df.dropna()
print("\nDataset After Removing Missing Values:")
print(df_removed)

df_filled = df.copy()
df_filled["Age"] = df_filled["Age"].fillna(df_filled["Age"].mean())
df_filled["Branch"] = df_filled["Branch"].fillna("Not Available")
df_filled["Marks"] = df_filled["Marks"].fillna(df_filled["Marks"].mean())

print("\nDataset After Filling Missing Values:")
print(df_filled)
