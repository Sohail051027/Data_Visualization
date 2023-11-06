
import pandas as pd
import matplotlib.pyplot as plt

# Load the salary dataset
salary_data = pd.read_csv('salary_visualization.csv')

# Map the education level to a more descriptive name
education_levels = {1: 'High School', 2: 'Bachelor’s Degree', 3: 'Master’s Degree', 4: 'Ph.D.'}
salary_data['Education Level'] = salary_data['Education Level'].map(education_levels)

# Define a color palette for the plots
color_palette = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6']

# Bar Chart: Average Salary by Gender
fig, ax = plt.subplots(figsize=(10, 8))
average_salary_by_gender = salary_data.groupby('Gender')['Salary'].mean().sort_values()
average_salary_by_gender.plot(kind='bar', color=color_palette[0:2], ax=ax)
ax.set_title('Average Salary by Gender', fontsize=20)
ax.set_xlabel('Gender', fontsize=16)
ax.set_ylabel('Average Salary ($)', fontsize=16)
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)
ax.legend(title='Gender', fontsize=14, title_fontsize='16')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()  

# Line Chart: Average Salary by Years of Experience
fig, ax = plt.subplots(figsize=(14, 8))
average_salary_by_experience = salary_data.groupby('Years of Experience')['Salary'].mean().sort_index()
average_salary_by_experience.plot(kind='line', marker='o', color=color_palette[2], ax=ax)
ax.set_title('Average Salary by Years of Experience', fontsize=20)
ax.set_xlabel('Years of Experience', fontsize=16)
ax.set_ylabel('Average Salary ($)', fontsize=16)
ax.tick_params(axis='both', labelsize=14)
ax.legend(title='Years of Experience', fontsize=14, title_fontsize='16')
plt.tight_layout()
plt.show()  # Show the second plot

# Scatter Plot: Salary vs Age
fig, ax = plt.subplots(figsize=(12, 8))
scatter = ax.scatter(salary_data['Age'], salary_data['Salary'], alpha=0.7, c=color_palette[3], s=100)
ax.set_title('Salary vs Age', fontsize=20)
ax.set_xlabel('Age', fontsize=16)
ax.set_ylabel('Salary ($)', fontsize=16)
ax.tick_params(axis='both', labelsize=14)
legend = ax.legend(['Age vs Salary'], fontsize=14, title_fontsize='16', loc='upper left')
plt.tight_layout()
plt.show()  # Show the third plot

# Boxplot: Salary Distribution by Education Level
fig, ax = plt.subplots(figsize=(12, 8))
salary_data.boxplot(column='Salary', by='Education Level', ax=ax, patch_artist=True, 
                    boxprops=dict(facecolor=color_palette[4], color=color_palette[4]),
                    medianprops=dict(color="yellow"))
ax.set_title('Salary Distribution by Education Level', fontsize=20)
ax.set_xlabel('Education Level', fontsize=16)
ax.set_ylabel('Salary ($)', fontsize=16)
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)
plt.suptitle('')  # Suppress the automatic title
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()  # Show the fourth plot

