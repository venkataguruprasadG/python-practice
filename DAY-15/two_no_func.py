'''
Challenge 71: Add Two Numbers Function
Write a function called add_numbers that:

Takes two numbers as arguments

Returns their sum

After defining the function:

Ask the user to input two numbers

Call the function with those numbers and print the result

Example:
text
Enter first number: 7
Enter second number: 13
Sum: 20
'''

def two_sum(num1,num2):
    return num1+num2

num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))

result=two_sum(num1,num2)

print(f"sum: {result}")