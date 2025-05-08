'''
Problem 37: Find Numbers Greater Than the Average
Write a Python program that:

Takes a list of integers as input from the user (space-separated).

Calculates the average of the numbers.

Finds and prints all numbers from the list that are strictly greater than the average, in the order they appeared.

Example:
Input:

text
Enter numbers: 10 20 30 40 50
Output:

text
Average: 30.0
Numbers greater than average: [40, 50]
'''

num_list = list(map(int, input("Enter numbers: ").split()))

total = sum(num_list)
avg = total / len(num_list)

new_list = []

for j in num_list:
    if j > avg:
        new_list.append(j)

print(f"Average: {avg}")
print(f"Numbers greater than average are: {new_list}")

