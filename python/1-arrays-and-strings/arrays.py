# 1. Creating and Initializing Arrays
from array import array

# Create an integer array
int_array = array('i', [1, 2, 3, 4, 5])
print("Integer Array:", int_array)

# Create a float array
float_array = array('f', [1.0, 2.5, 3.8])
print("Float Array:", float_array)

# 2. Basic Array Operations
# Access elements
print("First element:", int_array[0])
print("Last element:", int_array[-1])

# Modify elements
int_array[2] = 10
print("Modified Array:", int_array)

# Append elements
int_array.append(6)
print("After Append:", int_array)

# Remove elements
int_array.remove(10)
print("After Remove:", int_array)

# 3. Traversing Arrays
print("Array Traversal:")
for element in int_array:
    print(element, end=" ")
print()

# 4. Searching in Arrays
search_element = 4
if search_element in int_array:
    print(f"Element {search_element} found at index {int_array.index(search_element)}")
else:
    print(f"Element {search_element} not found")

# 5. Array Slicing
print("Sliced Array (1:4):", int_array[1:4])

# 6. Common Algorithms with Arrays
# Finding the maximum and minimum elements
max_element = max(int_array)
min_element = min(int_array)
print("Maximum Element:", max_element)
print("Minimum Element:", min_element)

# Calculating the sum of elements
array_sum = sum(int_array)
print("Sum of Array Elements:", array_sum)

# Reversing the array
reversed_array = int_array[::-1]
print("Reversed Array:", reversed_array)

# 7. Two-Dimensional Arrays using Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("2D Array (Matrix):")
for row in matrix:
    print(row)

# Accessing elements in a 2D array
print("Element at (1, 2):", matrix[1][2])  # Access row 1, column 2

# 8. Array Operations with Libraries (NumPy)
import numpy as np

# Create a NumPy array
np_array = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", np_array)

# Vectorized operations
np_array = np_array * 2
print("Doubled NumPy Array:", np_array)

# Reshaping arrays
matrix_np = np_array.reshape(1, 5)
print("Reshaped NumPy Array:")
print(matrix_np)

# 9. Sorting Arrays
sorted_array = sorted(int_array)
print("Sorted Array:", sorted_array)