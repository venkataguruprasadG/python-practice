'''
Problem 67: Prime Number Checker Function
Write a Python function that:

Takes an integer as input from the user.

Checks if the number is a prime number (a number greater than 1 that is only divisible by 1 and itself).

Prints "Prime" if it is, or "Not prime" if it isn’t.

Example 1:
Input:

text
Enter a number: 7
Output:

text
Prime
Example 2:
Input:

text
Enter a number: 10
Output:

text
Not prime
Hints:
A prime number has no divisors other than 1 and itself.

You only need to check divisibility up to the square root of the number.
'''

def isprime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
        return True
    
num=int(input("Enter a number: "))

if isprime(num):
    print("Prime")
else:
    print("Not Prime")