# Task 2: Indexing, Slicing and Reshaping
import numpy as np

arr = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])

print("Original Array:", arr)
print("First Element :", arr[0])
print("Last Element  :", arr[-1])
print("Element at Index 4:", arr[4])
print("\nSliced Array (Index 2 to 6):", arr[2:7])
print("Every Second Element:", arr[::2])

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(matrix)
print("Row 1:", matrix[1])
print("Column 2:", matrix[:, 2])
print("Element at Row 2, Column 3:", matrix[2, 3])

reshaped = arr.reshape(2, 5)
print("\nOriginal 1D Array:")
print(arr)
print("Reshaped Array (2 x 5):")
print(reshaped)
