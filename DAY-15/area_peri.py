'''
Challenge 73: Calculate Area and Perimeter of a Rectangle
Write a function called rectangle_info that:

Takes two arguments: length and width

Returns both the area and the perimeter of the rectangle

After defining the function:

Ask the user to input the length and width

Call the function using keyword arguments

Print both the area and perimeter

Example:
text
Enter length: 8
Enter width: 3
Area: 24
Perimeter: 22
Hints:
Area = length × width

Perimeter = 2 × (length + width)

To return two values, use: return area, perimeter

To call with keywords: rectangle_info(length=8, width=3)
'''

def rectangle_info(length,width):
    area=length*width
    perimeter=2*(length+width)
    return area,perimeter

length=int(input("Enter the length of the rectangle: "))
width=int(input("Enter the width of the rectangle: "))

area_result, perimeter_result=rectangle_info(length=length,width=width)

print(f"Area: {area_result}")
print(f"Perimeter: {perimeter_result}")
