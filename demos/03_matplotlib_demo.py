"""
PYTHON LIBRARIES SELF-LEARNING ACTIVITY
Demo 3: Matplotlib - Data Visualization Library
Author: [Your Name]
Date: December 18, 2025

Matplotlib is the foundation for creating charts and graphs in Python.
"""

import matplotlib.pyplot as plt
import numpy as np

print("="  * 60)
print("MATPLOTLIB DEMO - Data Visualization")
print("=" * 60)
print("\nThis demo creates 5 different charts.")
print("Each chart will open in a new window.")
print("Close each window to see the next chart.\n")

# 1. Simple Line Plot
print("1. Creating Line Plot - Programming Language Popularity Trends...")

years = [2020, 2021, 2022, 2023, 2024, 2025]
python_popularity = [70, 75, 80, 85, 90, 95]
java_popularity = [80, 78, 75, 72, 70, 68]
javascript_popularity = [75, 78, 80, 82, 85, 88]

plt.figure(figsize=(10, 6))
plt.plot(years, python_popularity, marker='o', label='Python', linewidth=2)
plt.plot(years, java_popularity, marker='s', label='Java', linewidth=2)
plt.plot(years, javascript_popularity, marker='^', label='JavaScript', linewidth=2)

plt.title('Programming Language Popularity (2020-2025)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Popularity Score', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('01_line_plot.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved as '01_line_plot.png'")
plt.show()

# 2. Bar Chart
print("\n2. Creating Bar Chart - Student Marks Comparison...")

students = ['Aman', 'Priya', 'Rahul', 'Sneha', 'Vikram']
marks = [85, 92, 78, 95, 88]
colors = ['skyblue', 'lightgreen', 'coral', 'gold', 'plum']

plt.figure(figsize=(10, 6))
bars = plt.bar(students, marks, color=colors, edgecolor='black', linewidth=1.5)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.title('Student Marks in Python Exam', fontsize=16, fontweight='bold')
plt.xlabel('Student Name', fontsize=12)
plt.ylabel('Marks', fontsize=12)
plt.ylim(0, 100)
plt.axhline(y=80, color='red', linestyle='--', label='Pass Mark (80)', alpha=0.7)
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('02_bar_chart.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved as '02_bar_chart.png'")
plt.show()

# 3. Pie Chart
print("\n3. Creating Pie Chart - Technology Usage Distribution...")

technologies = ['Python', 'Java', 'JavaScript', 'C++', 'Others']
usage_percentage = [30, 20, 25, 15, 10]
colors_pie = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
explode = (0.1, 0, 0, 0, 0)

plt.figure(figsize=(10, 8))
plt.pie(usage_percentage, labels=technologies, colors=colors_pie, 
        autopct='%1.1f%%', startangle=90, explode=explode,
        shadow=True, textprops={'fontsize': 12})
plt.title('Technology Usage in 2025', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('03_pie_chart.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved as '03_pie_chart.png'")
plt.show()

# 4. Scatter Plot
print("\n4. Creating Scatter Plot - Study Hours vs Marks...")

study_hours = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
exam_marks = [55, 60, 65, 70, 75, 80, 85, 90, 92, 95]

plt.figure(figsize=(10, 6))
plt.scatter(study_hours, exam_marks, c=exam_marks, cmap='viridis', 
            s=200, alpha=0.7, edgecolors='black', linewidth=1.5)
plt.colorbar(label='Marks')

z = np.polyfit(study_hours, exam_marks, 1)
p = np.poly1d(z)
plt.plot(study_hours, p(study_hours), "r--", alpha=0.8, linewidth=2, label='Trend Line')

plt.title('Study Hours vs Exam Marks', fontsize=16, fontweight='bold')
plt.xlabel('Study Hours per Day', fontsize=12)
plt.ylabel('Exam Marks', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('04_scatter_plot.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved as '04_scatter_plot.png'")
plt.show()

# 5. Dashboard
print("\n5. Creating Dashboard - Sales Data...")

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
laptop_sales = [15, 20, 18, 25, 30, 28]
phone_sales = [45, 50, 48, 55, 60, 58]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Sales Dashboard - First Half 2025', fontsize=18, fontweight='bold')

axes[0, 0].plot(months, laptop_sales, marker='o', color='blue', linewidth=2)
axes[0, 0].set_title('Laptop Sales Trend', fontweight='bold')
axes[0, 0].set_ylabel('Units Sold')
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].plot(months, phone_sales, marker='s', color='green', linewidth=2)
axes[0, 1].set_title('Phone Sales Trend', fontweight='bold')
axes[0, 1].set_ylabel('Units Sold')
axes[0, 1].grid(True, alpha=0.3)

revenue = [ls * 50000 + ps * 20000 for ls, ps in zip(laptop_sales, phone_sales)]
axes[1, 0].bar(months, revenue, color='orange', edgecolor='black')
axes[1, 0].set_title('Total Revenue', fontweight='bold')
axes[1, 0].set_ylabel('Revenue (₹)')
axes[1, 0].grid(axis='y', alpha=0.3)

axes[1, 1].plot(months, laptop_sales, marker='o', label='Laptops', linewidth=2)
axes[1, 1].plot(months, phone_sales, marker='s', label='Phones', linewidth=2)
axes[1, 1].set_title('Laptop vs Phone Sales', fontweight='bold')
axes[1, 1].set_ylabel('Units Sold')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('05_dashboard.png', dpi=300, bbox_inches='tight')
print("   ✓ Saved as '05_dashboard.png'")
plt.show()

print("\n" + "=" * 60)
print("Matplotlib Demo Complete!")
print("All charts saved as PNG files!")
print("=" * 60)