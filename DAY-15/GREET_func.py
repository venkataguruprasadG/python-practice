'''
Challenge 70: Personalized Greeting Function
Write a function called greet_user that:

Takes a user’s name as input (as a function argument)

Returns the string: "Hello, <name>! Welcome to Python programming."

Print the returned string after calling the function

Example:
python
def greet_user(name):
    # Your code here

message = greet_user("Amit")
print(message)
Output:

text
Hello, Amit! Welcome to Python programming.
'''

def greet_user(name):
    return f"Hello, {name}! Welcome to python programming."    
    
msg=greet_user("Guru")
print(msg)

