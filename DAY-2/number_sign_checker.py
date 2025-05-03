#Problem 3: Number Sign Checker
#Problem Statement
#Write a Python program that:

#Asks the user to enter a number.

#Checks whether the number is positive, negative, or zero.

#Prints one of the following messages based on the input:

#Positive

#Negative

#Zero

num = int(input("Dear user enter the number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
    