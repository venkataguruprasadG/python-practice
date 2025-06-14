'''
Exercise
Try this:

Create a list named colors with 5 color names.

Print the first and last color using indexing.

Replace the second color with a different one.

Append a new color to the list.

Reverse the list and print it.
'''

colors = ['red','yellow','orange','blue','white']

print(f"first color: {colors[0]}")

print(f"Last color: {colors[-1]}")

colors[1]='green'

colors.append('light blue')

print(f"reverse of the list colors: {colors[::-1]}")