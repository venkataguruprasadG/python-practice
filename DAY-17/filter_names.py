'''
Challenge 81: Filter Names by First Letter
Write a function called filter_names that:

Takes a list of names and a letter as arguments

Returns a list of names that start with the given letter (case-insensitive)

After defining the function:

Call it with ["Amit", "Rahul", "Sara", "Anu", "Ravi"] and the letter "A"

Print the result

Expected Output:
text
['Amit', 'Anu']
Hints:
Use filter() and a lambda function inside your function

Use name.lower().startswith(letter.lower()) for case-insensitive matching
'''

def filter_names(names, letter):
    return list(filter(lambda name: name.lower().startswith(letter.lower()),names))

names_list=["Amit", "Rahul", "Sara"]
result=filter_names(names_list, "A")
print(result)

