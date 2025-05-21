"""
Challenge 84: Remove Duplicate Characters
Write a function called remove_duplicates that:

Accepts a string as input.

Returns a new string with all duplicate characters removed, keeping only the first occurrence of each character.

For example:

Input: "programming"

Output: "progamin"

Input: "banana"

Output: "ban"

"""
def remove_duplicates(str):
    result=""
    for i in str:
        if i not in result:
            result += i
    
    return result

print(remove_duplicates("banana"))