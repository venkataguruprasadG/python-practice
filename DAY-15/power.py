'''
Challenge 72: Power Function with Default Exponent
Write a function called power that:

Takes two arguments: base and exponent

The exponent argument should have a default value of 2

Returns the result of raising base to the power of exponent

After defining the function:

Ask the user to input a base number

Ask the user to optionally input an exponent (if they don’t, use the default)

Print the result

Example 1:
text
Enter base number: 5
Enter exponent (press Enter to use default 2): 
Result: 25

Hints:
Use input() for the exponent and check if the user entered a value.

Use int() only if the input is not empty.
'''

def power(base, exponent=2):
    return base ** exponent

base=int(input("Enter you base number: "))
exponent_input=int(input("Enter your exponent value: "))

if exponent_input=="":
    result=power(base)
else:
    result=power(base, int(exponent_input))

print("Result: ",result)
