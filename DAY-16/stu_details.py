'''
Challenge 76: Print Student Details with **kwargs
Write a function called print_student_details that:

Accepts any number of keyword arguments using **kwargs

Prints each key and its value in the format: key: value

After defining the function:

Call the function with:

name="Amit", age=22, course="Python"

name="Sara", age=20, course="Java", city="Delhi"

Example Output:
text
name: Amit
age: 22
course: Python

name: Sara
age: 20
course: Java
city: Delhi
Hints:
Use a for loop to iterate over kwargs.items()

Print a blank line between calls for clar
'''

def print_student_details(*kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print()

print_student_details(name="amit",age="22",Course="Python")