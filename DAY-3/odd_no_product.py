'''
Problem 6: Odd Number Product
Write a Python program that calculates the product of all odd numbers from 1 to n (inclusive).

Test Case:
Input: 5 → Output: 1 * 3 * 5 = 15
'''

n = int(input("Enter the number range: "))
pro = 1
odd_numbers = []

for i in range(1, n+1):
    if i % 2 != 0:
        pro *= i
        odd_numbers.append(str(i))

print(" * ".join(odd_numbers), "=", pro)




       
