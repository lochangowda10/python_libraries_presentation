
"""
PYTHON LIBRARIES SELF-LEARNING ACTIVITY
Demo 5: Combined Example - All Libraries Working Together
Author: [Your Name]
Date: December 18, 2025
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 80)
print("COMBINED DEMO - Student Performance Analysis System")
print("Using: NumPy + Pandas + Matplotlib")
print("=" * 80)

# Step 1: Generate Data with NumPy
print("\n📊 STEP 1: Generating Student Data with NumPy")
print("-" * 80)

np.random.seed(42)
num_students = 20

math_marks = np.random.randint(60, 100, num_students)
science_marks = np.random.randint(65, 98, num_students)
english_marks = np.random.randint(70, 95, num_students)
attendance = np.random.randint(70, 101, num_students)

print(f"✓ Generated data for {num_students} students")

# Step 2: Create DataFrame with Pandas
print("\n📋 STEP 2: Organizing Data with Pandas")
print("-" * 80)

df = pd.DataFrame({
    'Student_ID': range(1001, 1001 + num_students),
    'Math': math_marks,
    'Science': science_marks,
    'English': english_marks,
    'Attendance': attendance
})

df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1).round(2)

def assign_grade(avg):
    if avg >= 90: return 'A+'
    elif avg >= 80: return 'A'
    elif avg >= 70: return 'B'
    else: return 'C'

df['Grade'] = df['Average'].apply(assign_grade)
df['Status'] = df['Average'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')

print("First 5 students:")
print(df.head())

# Step 3: Analysis
print("\n📈 STEP 3: Statistical Analysis")
print("-" * 80)

print(f"Total Students: {len(df)}")
print(f"Pass: {len(df[df['Status'] == 'Pass'])}")
print(f"Average Math: {df['Math'].mean():.2f}")
print(f"Average Science: {df['Science'].mean():.2f}")
print(f"Average English: {df['English'].mean():.2f}")

# Step 4: Visualization with Matplotlib
print("\n📊 STEP 4: Creating Visualizations")
print("-" * 80)

fig = plt.figure(figsize=(16, 12))

# Chart 1: Subject Averages
ax1 = plt.subplot(2, 2, 1)
subjects = ['Math', 'Science', 'English']
avgs = [df['Math'].mean(), df['Science'].mean(), df['English'].mean()]
bars = ax1.bar(subjects, avgs, color=['#FF6B6B', '#4ECDC4', '#45B7D1'], edgecolor='black')
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height, f'{height:.1f}',
             ha='center', va='bottom', fontweight='bold')
ax1.set_title('Average Marks by Subject', fontsize=14, fontweight='bold')
ax1.set_ylabel('Average Marks')
ax1.grid(axis='y', alpha=0.3)

# Chart 2: Grade Distribution
ax2 = plt.subplot(2, 2, 2)
grade_counts = df['Grade'].value_counts()
ax2.pie(grade_counts.values, labels=grade_counts.index, autopct='%1.1f%%',
        startangle=90, textprops={'fontweight': 'bold'})
ax2.set_title('Grade Distribution', fontsize=14, fontweight='bold')

# Chart 3: Attendance vs Performance
ax3 = plt.subplot(2, 2, 3)
scatter = ax3.scatter(df['Attendance'], df['Average'], c=df['Average'],
                     cmap='RdYlGn', s=150, edgecolors='black')
plt.colorbar(scatter, ax=ax3, label='Average Marks')
z = np.polyfit(df['Attendance'], df['Average'], 1)
p = np.poly1d(z)
ax3.plot(df['Attendance'], p(df['Attendance']), "r--", linewidth=2, label='Trend')
ax3.set_title('Attendance vs Performance', fontsize=14, fontweight='bold')
ax3.set_xlabel('Attendance (%)')
ax3.set_ylabel('Average Marks')
ax3.legend()
ax3.grid(True, alpha=0.3)

# Chart 4: Pass/Fail
ax4 = plt.subplot(2, 2, 4)
status = df['Status'].value_counts()
bars = ax4.bar(status.index, status.values, color=['#2ECC71', '#E74C3C'], edgecolor='black')
for bar in bars:
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height, f'{int(height)}',
             ha='center', va='bottom', fontsize=12, fontweight='bold')
ax4.set_title('Pass/Fail Distribution', fontsize=14, fontweight='bold')
ax4.set_ylabel('Number of Students')
ax4.grid(axis='y', alpha=0.3)

plt.suptitle('Student Performance Analysis Dashboard', fontsize=18, fontweight='bold')
plt.tight_layout()
plt.savefig('student_analysis_dashboard.png', dpi=300, bbox_inches='tight')
print("✓ Dashboard saved as 'student_analysis_dashboard.png'")
plt.show()

# Step 5: Export Data
print("\n💾 STEP 5: Exporting Results")
print("-" * 80)

df.to_csv('student_performance_report.csv', index=False)
print("✓ Complete report saved to 'student_performance_report.csv'")

top_10 = df.nlargest(10, 'Average')
top_10.to_csv('top_10_students.csv', index=False)
print("✓ Top 10 students saved to 'top_10_students.csv'")

summary = pd.DataFrame([{
    'Total_Students': len(df),
    'Pass_Count': len(df[df['Status'] == 'Pass']),
    'Class_Average': round(df['Average'].mean(), 2)
}])
summary.to_csv('class_summary.csv', index=False)
print("✓ Summary saved to 'class_summary.csv'")

print("\n" + "=" * 80)
print("🎉 ANALYSIS COMPLETE!")
print("=" * 80)
print("\nThis demo showed how NumPy, Pandas, and Matplotlib work together!")

