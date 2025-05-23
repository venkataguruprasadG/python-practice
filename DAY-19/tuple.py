'''
Challenge 92: Sort Tuples by Second Value
Task:
Given a list of tuples, each containing two numbers, use a lambda function to sort the list by the second value in each tuple.
'''

pairs = [(3, 7), (1, 5), (4, 2), (9, 8)]

# Sort using lambda to get the second value of each tuple
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])

print(sorted_pairs)  # Output: [(4, 2), (1, 5), (3, 7), (9, 8)]
