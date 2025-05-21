"""
Challenge 83: Double Each Character
Write a Python function called double_characters that:

Accepts a string as input.

Returns a new string where every character from the original string is doubled.

For example:

If you pass "now", the function should return "nnooww".

If you pass "123a!", the function should return "112233aa!!".
"""

def double_characters(str1):
    return "".join([x*2 for x in str1])

print(double_characters("now"))