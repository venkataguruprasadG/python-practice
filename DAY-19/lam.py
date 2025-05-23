'''
Challenge 89: Lambda Power
Write a lambda function called power that:

Accepts two arguments: base and exponent.

Returns base raised to the exponent.

Example:

Input: power(2, 3)

Output: 8

Bonus:
Use this lambda with map() to calculate powers for a list of exponents:
'''

power = lambda base, exponent: base ** exponent

print(power(2,4))