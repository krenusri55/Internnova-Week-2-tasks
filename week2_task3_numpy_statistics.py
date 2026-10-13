# Task 3: Mathematical and Statistical Operations
import numpy as np

marks = np.array([78, 85, 92, 67, 88, 95, 73, 81, 90, 84])
bonus = np.array([2, 3, 1, 4, 2, 5, 3, 1, 2, 4])

print("Marks Array:", marks)
print("Bonus Array:", bonus)

print("\n--------- MATHEMATICAL OPERATIONS ---------")
print("Addition       :", marks + bonus)
print("Subtraction    :", marks - bonus)
print("Multiplication :", marks * 2)
print("Division       :", np.round(marks / 2, 2))

print("\n--------- STATISTICAL OPERATIONS ---------")
print("Mean              :", np.mean(marks))
print("Median            :", np.median(marks))
print("Minimum Marks     :", np.min(marks))
print("Maximum Marks     :", np.max(marks))
print("Standard Deviation:", np.round(np.std(marks), 2))
print("Sum of Marks      :", np.sum(marks))
