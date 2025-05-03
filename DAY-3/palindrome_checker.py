'''
Problem 9: Palindrome Checker
Write a Python program that takes a string as input and checks if it is a palindrome (the same forwards and backwards, ignoring case). Print "Yes" if it is a palindrome, otherwise print "No".

Test Case:
Input: Madam → Output: Yes
Input: python → Output: No
'''

s=input("Enter your string: ")

if s.lower() == s.lower()[::-1]:
    print(f"Yes the given string {s} is a palindrome")
else:
    print("No")