'''
Challenge 74: Student Info Function
Write a function called student_info that:

Takes three arguments: name, age, and course

The course argument should have a default value of "Python"

Prints the student’s name, age, and course in a formatted way

After defining the function:

Call the function twice:

Once with all three arguments (using keyword arguments)

Once with only name and age (so it uses the default course)

Example Output:
text
Name: Rahul, Age: 21, Course: Java
Name: Priya, Age: 19, Course: Python
'''

def student_info(name, age, course="python"):
    print(f"Name: {name}, Age: {age}, Course: {course}")

student_info(name="Rahul", age=21, course="Java")

student_info(name="Priya", age=23)
