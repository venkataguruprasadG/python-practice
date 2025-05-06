'''
Problem 27: Student Grades Summary
Write a Python program that:

Takes the number of students as input.

For each student, takes their name and a list of grades (space-separated integers).

Stores each student’s grades in a dictionary with the student’s name as the key.

After all data is entered, prints:

The student(s) with the highest average grade (if there’s a tie, print all names sorted alphabetically).

The highest average grade (rounded to 2 decimal places).

Example:
Input:

text
Enter number of students: 3
Enter name of student 1: Alice
Enter grades for Alice (space-separated): 90 95 100
Enter name of student 2: Bob
Enter grades for Bob (space-separated): 80 85 90
Enter name of student 3: Carol
Enter grades for Carol (space-separated): 95 100 90
Output:

text
Top student(s): ['Alice', 'Carol']
Highest average grade: 95.0
'''

num_students = int(input("Enter number of students: "))

grades_dict = {}

# Collect names and grades for each student
for i in range(1, num_students + 1):
    name = input(f"Enter name of student {i}: ")
    grades_input = input(f"Enter grades for {name} (space-separated): ")
    grades = [int(x) for x in grades_input.split()]
    grades_dict[name] = grades

# Calculate averages for each student
averages = {}
for name, grades in grades_dict.items():
    avg = sum(grades) / len(grades)
    averages[name] = avg

# Find the highest average
highest_avg = max(averages.values())

# Collect all students with the highest average
top_students = [name for name, avg in averages.items() if avg == highest_avg]
top_students.sort()  # Sort alphabetically

# Print results
print(f"Top student(s): {top_students}")
print(f"Highest average grade: {round(highest_avg, 2)}")

