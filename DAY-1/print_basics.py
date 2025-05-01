#Problem 1: Print Basics
#Task: Write a program that prints "Hello, Cisco!" and then asks the user for their name, printing "Welcome, [Name]!".

#Test Cases:

#Input: Alice → Output:

#text
#Hello, Cisco!  
#Welcome, Alice!
#Input: Bob → Output:

#text
#Hello, Cisco!  
#Welcome, Bob!
#Interview Theory:

#print(): Function to output text. Use print("text") or print(variable).

#input(): Captures user input. Always returns a string (e.g., name = input("Enter name: ")).

print("Hello, cisco")
name=input("Enter your name: ")
print("Welcome, "+name)

