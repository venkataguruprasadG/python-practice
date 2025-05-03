'''
Problem 11: Factorial Calculation
Write a Python program that takes a positive integer n as input and prints the factorial of n. (The factorial of n is the product of all positive integers from 1 to n, denoted as n!.)

Test Case:
Input: 5 → Output: 120
Input: 3 → Output: 6
'''

n = int(input("Enter your number: "))

if n > 0:
    product = 1
    for i in range(1, n+1):
        product *= i
    print(product)
else:
    print("Please enter a positive integer.")


