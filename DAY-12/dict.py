'''
Problem 55: Frequency Table of Numbers in a List
Write a Python program that:

Takes a list of numbers as input from the user (separated by spaces).

Counts how many times each unique number appears in the list.

Prints each number along with its frequency.

Example 1:
Input:

text
Enter numbers: 2 3 2 5 3 2 4
Output:

text
2 appears 3 times
3 appears 2 times
5 appears 1 time
4 appears 1 time
Example 2:
Input:

text
Enter numbers: 10 10 20
Output:

text
10 appears 2 times
20 appears 1 time
Hints:
Use a dictionary to store counts for each number.

Remember to convert the input numbers to integers.

Loop through the dictionary to print the results.
'''

num_list=input("Enter your numbers: ").split()

num_dict={}

num_list_int=[int(num) for num in num_list]

for num in num_list_int:
    if num in num_dict:
        num_dict[num]+=1
    else:
        num_dict[num]=1

for num, value in num_dict.items():
    print(f"{num} appears {value} times")