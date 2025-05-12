'''
Problem 54: Count Occurrences of a Number in a List
Write a Python program that:

Takes a list of numbers as input from the user (separated by spaces).

Asks the user for a number to search for.

Counts and prints how many times that number appears in the list.

Example 1:
Input:

text
Enter numbers: 1 2 3 2 4 2 5
Enter the number to count: 2
Output:

text
2 appears 3 times in the list.
Example 2:
Input:

text
Enter numbers: 10 20 30 40
Enter the number to count: 25
Output:

text
25 appears 0 times in the list.
Hints:
Use .split() and convert inputs to integers.

Use the .count() method or a loop to count occurrences.
'''

num=input("Enter your numbers: ").split()

num=[int(n) for n in num]

num_input=int(input("Enter your number: "))

count=num.count(num_input)

print(f"{num_input} appears {count} times in the list")
