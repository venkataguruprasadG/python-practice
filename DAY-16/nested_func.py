'''
Challenge 78: Nested Function for Addition
Write a program with the following requirements:

Define an outer function that accepts two parameters, a and b.

Inside the outer function, define an inner function that calculates the sum of a and b.

The outer function should then add 5 to this sum.

Finally, the outer function should return the resulting value.

Example:

If you call your outer function with (5, 10), the output should be 20 (because 5 + 10 = 15, then 15 + 5 = 20).

'''

def outer_func(a, b):
    def inner_func():
        return a+b
    result=inner_func() + 5
    return result

result=outer_func(5, 10)
print(result)