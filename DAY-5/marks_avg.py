'''
Problem 24: Student Marks Average Calculator

Write a Python program that:

Takes input for the number of students.

For each student, takes the student’s name and a list of their marks (space-separated).

Stores this data in a dictionary, where the key is the student’s name and the value is a list of their marks.

After all input, prints each student’s name and their average mark (rounded to 2 decimal places).

Example:
Input:

text
Enter number of students: 2
Enter name of student 1: Alice
Enter marks for Alice (space-separated): 80 90 100
Enter name of student 2: Bob
Enter marks for Bob (space-separated): 70 85 90
Output:

text
Alice: 90.0
Bob: 81.67
'''

num=int(input("Enter number of students: "))

stu_dict={}

for i in range(1,num+1):
    stu_name = input(f"Enter name of student {i}: ")
    stu_marks=input(f"Enter marks for {stu_name} (space-separated): ")
    stu_marks = [int(x) for x in stu_marks.split()]
    stu_dict[stu_name] = stu_marks

for stu_name,stu_marks in stu_dict.items():
    print(f"Student name: {stu_name} {stu_marks}")
    avg = round(sum(stu_marks) / len(stu_marks), 2)
    print(f"{stu_name}: {avg}")




print(stu_dict)

