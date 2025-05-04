'''
Problem 13:
Write a Python program that takes 5 numbers (one per line) and prints their average.

Hint:

Use a loop to collect the numbers in a list.

Calculate the sum and divide by the count.
'''

s = input("Enter numbers: ")
n = s.split()

total = 0
for i in n:
    total += int(i)  # or float(i) for decimals

average = total / len(n)
print("Average:", average)

