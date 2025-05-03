'''
Problem 10: Sum of Digits
Write a Python program that takes a positive integer as input and calculates the sum of its digits. Print the sum.

Test Case:
Input: 1234 → Output: 10
Input: 505 → Output: 10
'''

n=int(input("Enter your number: "))
 
if n<0:
    print("Please enter the positive integer")
else:
    total=0
    for digit in str(n):
        total+=int(digit)
    print(total)


