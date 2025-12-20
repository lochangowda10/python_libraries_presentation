"""
PYTHON LIBRARIES SELF-LEARNING ACTIVITY
Demo 1: NumPy - Numerical Python Library
Author: [Your Name]
Date: December 18, 2025

NumPy is the foundation for scientific computing in Python.
It provides fast operations on arrays and mathematical functions.
"""

import numpy as np

print("=" * 60)
print("NUMPY DEMO - Array Operations and Mathematical Functions")
print("=" * 60)

# 1. Creating Arrays
print("\n1. CREATING ARRAYS:")
print("-" * 40)

# Simple array
simple_array = np.array([10, 20, 30, 40, 50])
print(f"Simple Array: {simple_array}")
print(f"Type: {type(simple_array)}")

# 2D Array (Matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D Array (Matrix):\n{matrix}")

# Array of zeros
zeros = np.zeros(5)
print(f"\nArray of zeros: {zeros}")

# Array of ones
ones = np.ones((3, 3))
print(f"\nArray of ones:\n{ones}")

# Range of numbers
range_array = np.arange(0, 10, 2)  # Start, Stop, Step
print(f"\nRange array (0 to 10, step 2): {range_array}")

# 2. Basic Mathematical Operations
print("\n2. MATHEMATICAL OPERATIONS:")
print("-" * 40)

numbers = np.array([10, 20, 30, 40, 50])
print(f"Original array: {numbers}")
print(f"Mean (Average): {numbers.mean()}")
print(f"Sum: {numbers.sum()}")
print(f"Maximum: {numbers.max()}")
print(f"Minimum: {numbers.min()}")
print(f"Standard Deviation: {numbers.std():.2f}")

# 3. Array Arithmetic (Much faster than Python lists!)
print("\n3. ARRAY ARITHMETIC:")
print("-" * 40)

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([10, 20, 30, 40, 50])

print(f"Array 1: {array1}")
print(f"Array 2: {array2}")
print(f"Addition (element-wise): {array1 + array2}")
print(f"Multiplication (element-wise): {array1 * array2}")
print(f"Array 1 multiplied by 10: {array1 * 10}")
print(f"Array 1 squared: {array1 ** 2}")

# 4. Real-World Example: Student Marks Analysis
print("\n4. REAL-WORLD USE CASE - STUDENT MARKS ANALYSIS:")
print("-" * 40)

# Marks of 5 students in 3 subjects
student_marks = np.array([
    [85, 90, 78],  # Student 1
    [92, 88, 95],  # Student 2
    [76, 82, 80],  # Student 3
    [88, 85, 90],  # Student 4
    [95, 92, 98]   # Student 5
])

print("Marks of 5 students in 3 subjects:")
print(student_marks)

print(f"\nAverage marks of each student:")
for i, avg in enumerate(student_marks.mean(axis=1), 1):
    print(f"  Student {i}: {avg:.2f}")

print(f"\nAverage marks in each subject:")
subject_names = ["Math", "Science", "English"]
for subject, avg in zip(subject_names, student_marks.mean(axis=0)):
    print(f"  {subject}: {avg:.2f}")

print(f"\nOverall class average: {student_marks.mean():.2f}")
print(f"Highest marks in class: {student_marks.max()}")
print(f"Lowest marks in class: {student_marks.min()}")

# 5. Why NumPy is Important
print("\n5. WHY USE NUMPY?")
print("-" * 40)
print("✓ 50-100x faster than Python lists for numerical operations")
print("✓ Used by: Data Science, Machine Learning, Image Processing")
print("✓ Foundation for: Pandas, SciPy, Matplotlib, TensorFlow")
print("✓ Real-world applications: Financial analysis, Scientific research")

print("\n" + "=" * 60)
print("NumPy Demo Complete!")
print("=" * 60)