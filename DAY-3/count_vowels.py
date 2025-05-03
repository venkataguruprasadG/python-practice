'''
Problem 8: Count Vowels
Write a Python program that takes a string as input and counts the number of vowels (a, e, i, o, u, both uppercase and lowercase) in the string. Print the count.

Test Case:
Input: Hello World → Output: 3
'''

s=input("Enter a string: ")

count=0

for char in s:
    if char in "aeiouAEIOU":
        count+= 1
print(count)

