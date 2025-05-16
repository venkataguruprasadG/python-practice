'''
Challenge 77: Mixed Arguments Function
Write a function called mixed_args_demo that:

Accepts any number of positional arguments (*args)

Accepts any number of keyword arguments (**kwargs)

Prints all positional arguments on one line, separated by spaces

Prints all keyword arguments in the format: key: value (one per line)

After defining the function:

Call the function with:

1, 2, 3, name="Amit", age=22

"apple", "banana", city="Delhi", country="India"

Example Output:
text
Positional arguments: 1 2 3
Keyword arguments:
name: Amit
age: 22

Positional arguments: apple banana
Keyword arguments:
city: Delhi
country: India
Hints:
Use " ".join(str(arg) for arg in args) to print positional arguments

Use a for loop to print kwargs.items()

Print a blank line between calls for clarity
'''

def mixed_args_demo(*args, **kwargs):
    # Print positional arguments
    print("Positional arguments:", " ".join(str(arg) for arg in args))
    
    # Print keyword arguments
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print()  # Blank line for clarity

# Call the function with different arguments
mixed_args_demo(1, 2, 3, name="Amit", age=22)
mixed_args_demo("apple", "banana", city="Delhi", country="India")
