'''
Challenge 85: Find Common Elements
Write a function called common_elements that:

Accepts two lists as arguments.

Returns a new list containing only the elements that appear in both lists (no duplicates).

For example:

Input: `[1,nd ``

Output: ``

Input: ["apple", "banana", "cherry"] and ["banana", "date", "fig", "cherry"]

Output: ["banana", "cherry"]
'''

def common_ele(list1, list2):
    return [x for x in list1 if x in list2]

print(common_ele(["apple","banana"],["banana","date","fig"]))