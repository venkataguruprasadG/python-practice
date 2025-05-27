'''
Mini Project: Build a Simple Calculator

Let’s apply what we’ve learned!

Task: Build a calculator that asks the user to enter two numbers and an operator, then prints the result.

Approach

1. Take two numbers from the user.
2. Ask for an operator (+, -, *, /).
3. Perform the operation based on what the user entered.
4. Print the result, or shows "Invalid operator!" if the input is wrong.
'''

a = int(input("Enter your 1st number here: "))

b = int(input("Enter your 2nd number here: "))

action = input("Enter the action which you want to perform (add||subtract||multiply||division)")

if action == 'add':
    print(a+b)
elif action == 'subtract':
    print(a-b)
elif action == 'multiply':
    print(a*b)
elif action == 'division':
    if b == 0:
        print("Division can be performed here")
    else:
        print(a/b)
else:
    print("Enter the correct action code word to perform the operations...!!!!") 