'''
Challenge 75: Sum of All Numbers Function
Write a function called sum_all that:

Accepts any number of numeric arguments using *args

Returns the sum of all the arguments

After defining the function:

Call the function with:

Three numbers (e.g., sum_all(2, 4, 6))

Five numbers (e.g., sum_all(1, 2, 3, 4, 5))

Print the results

Example Output:
text
Sum 1: 12
Sum 2: 15
Hints:
Use the built-in sum() function on args

Remember, *args collects arguments as a tuple
'''

def sum_all(*args):
    return sum(args)

# Call the function and print the results
result1 = sum_all(2, 4, 6)
result2 = sum_all(1, 2, 3, 4, 5)

print("Sum 1:", result1)
print("Sum 2:", result2)
