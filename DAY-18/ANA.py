'''
Challenge 82: Check for Anagrams
Write a function called are_anagrams that:

Accepts two strings as arguments.

Returns True if the two strings are anagrams of each other (contain the same characters in any order), and False otherwise.

After defining the function:

Call it with "listen" and "silent" (should return True)

Call it with "hello" and "world" (should return False)

Print the results

Example Output:
text
True
False
'''

def ana(string1, string2):
    return sorted(string1.lower()) == sorted(string2.lower())

ana("hello", "world")