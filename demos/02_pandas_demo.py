"""
PYTHON LIBRARIES SELF-LEARNING ACTIVITY
Demo 2: Pandas - Data Analysis Library
Author: [Your Name]
Date: December 18, 2025

Pandas is the most popular library for data manipulation and analysis.
It provides DataFrames (like Excel tables) for working with structured data.
"""

import pandas as pd
import numpy as np

print("=" * 60)
print("PANDAS DEMO - Data Analysis with DataFrames")
print("=" * 60)

# 1. Creating DataFrames
print("\n1. CREATING DATAFRAMES:")
print("-" * 40)

# From a dictionary
student_data = {
    'Name': ['Aman', 'Priya', 'Rahul', 'Sneha', 'Vikram'],
    'Roll_No': [101, 102, 103, 104, 105],
    'Marks': [85, 92, 78, 95, 88],
    'Subject': ['Python', 'Python', 'Python', 'Python', 'Python']
}

df = pd.DataFrame(student_data)
print("Student DataFrame:")
print(df)

# 2. Basic DataFrame Operations
print("\n2. VIEWING DATA:")
print("-" * 40)

print("\nFirst 3 rows:")
print(df.head(3))

print("\nDataFrame Info:")
print(df.info())

print("\nBasic Statistics:")
print(df.describe())

# 3. Accessing Data
print("\n3. ACCESSING DATA:")
print("-" * 40)

print("\nAll Names:")
print(df['Name'].values)

print("\nStudent with highest marks:")
top_student = df[df['Marks'] == df['Marks'].max()]
print(top_student)

print("\nStudents who scored above 85:")
high_scorers = df[df['Marks'] > 85]
print(high_scorers)

# 4. Adding New Columns
print("\n4. ADDING CALCULATIONS:")
print("-" * 40)

# Add grade column based on marks
def assign_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    else:
        return 'C'

df['Grade'] = df['Marks'].apply(assign_grade)
print("\nDataFrame with Grades:")
print(df)

# 5. Real-World Example: Sales Data Analysis
print("\n5. REAL-WORLD USE CASE - SALES DATA ANALYSIS:")
print("-" * 40)

sales_data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Laptop', 'Phone', 'Tablet'],
    'Month': ['Jan', 'Jan', 'Jan', 'Jan', 'Feb', 'Feb', 'Feb'],
    'Units_Sold': [15, 45, 30, 80, 20, 50, 35],
    'Price': [50000, 20000, 30000, 2000, 50000, 20000, 30000]
}

sales_df = pd.DataFrame(sales_data)
sales_df['Revenue'] = sales_df['Units_Sold'] * sales_df['Price']

print("Sales Data with Revenue:")
print(sales_df)

print("\nTotal Revenue by Product:")
product_revenue = sales_df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
print(product_revenue)

print("\nTotal Revenue by Month:")
month_revenue = sales_df.groupby('Month')['Revenue'].sum()
print(month_revenue)

print(f"\nBest Selling Product: {product_revenue.index[0]}")
print(f"Total Revenue: ₹{sales_df['Revenue'].sum():,}")

# 6. Working with CSV Files (Example code)
print("\n6. READING/WRITING CSV FILES:")
print("-" * 40)
print("Code to read CSV file:")
print("  df = pd.read_csv('data.csv')")
print("\nCode to save to CSV file:")
print("  df.to_csv('output.csv', index=False)")

# Save our student data as example
df.to_csv('student_data.csv', index=False)
print("\n✓ Student data saved to 'student_data.csv'")

# Read it back
df_read = pd.read_csv('student_data.csv')
print("\n✓ Data read back from CSV:")
print(df_read.head())

# 7. Data Cleaning Example
print("\n7. DATA CLEANING:")
print("-" * 40)

# Create data with missing values
messy_data = {
    'Name': ['John', 'Sarah', None, 'Mike', 'Emma'],
    'Age': [25, None, 30, 28, 22],
    'Salary': [50000, 60000, None, 55000, 48000]
}

messy_df = pd.DataFrame(messy_data)
print("Data with missing values:")
print(messy_df)

print("\nMissing values count:")
print(messy_df.isnull().sum())

# Fill missing values
cleaned_df = messy_df.fillna({
    'Name': 'Unknown',
    'Age': messy_df['Age'].mean(),
    'Salary': messy_df['Salary'].mean()
})

print("\nCleaned data:")
print(cleaned_df)

# 8. Why Pandas is Important
print("\n8. WHY USE PANDAS?")
print("-" * 40)
print("✓ Handle data like Excel, but much more powerful")
print("✓ Read/Write: CSV, Excel, SQL databases, JSON")
print("✓ Clean messy data easily")
print("✓ Used by: Data Analysts, Data Scientists, Researchers")
print("✓ Real-world: Sales analysis, Student records, Financial data")

print("\n" + "=" * 60)
print("Pandas Demo Complete!")
print("=" * 60)