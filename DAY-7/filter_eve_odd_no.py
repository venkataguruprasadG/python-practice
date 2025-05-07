'''
Write a Python program that:

Takes a list of integers as input from the user (space-separated).

Separates the numbers into two lists: one for even numbers and one for odd numbers.

Prints both lists in ascending order.

Example:
Input:

text
Enter numbers: 5 8 3 2 9 4 7 6
Output:

text
Even numbers: [2, 4, 6, 8]
Odd numbers: [3, 5, 7, 9]
'''

num=input("Enter your numbers: ")

num_list=[int(x) for x in num.split()]

odd_list=[]

eve_list=[]

for i in num_list:
    if i%2==0:
        eve_list.append(i)
    else:
        odd_list.append(i)

odd_list.sort()
eve_list.sort()

print(f"Odd numbers list: {odd_list}")
print(f"Even numbers list: {eve_list}")

