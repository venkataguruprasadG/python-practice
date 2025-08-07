import numpy as np

arr = np.array([10,20,30,40,50])

print("Array: ", arr)

print("Array size: ", arr.size)

print("Array Data Type: ", arr.dtype)

#Array slicing and indexing

print("First three elements: ", arr[:3])

print("Last two elements: ". arr[-2:])

print("In reverse order of the array: ", arr[::-1])

#2D ARRAY 

arr1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("Print Second Row: ", arr1[1])

print("Ele at row 3 column 2: ", arr1[2,1])

#ARITHMETIC OPERATIONS

a = np.array([10,20,30,40])
b = np.array([20,30,40,50])

print(a+b)
print(a-b)
print(a**b)
print(a>2)

data = np.array([[10, 20], [30, 40], [50, 60]])

print("mean of the array:",np.mean(data))
print("sum of all the elements: ",np.sum(data))
print("maximum of all the array: ",np.max(data))
print("Minimum of all the array: ",np.min(data))
print("Mean of each column: ",np.mean(data, axis=0))

#GENERATE RANDOM NUMBERS

arr3 = np.random.randint(1, 101, size =5)
print(arr3)

#sort this array

sorted_arr3 = np.sort(arr3) 
print("sorted array: ",sorted_arr3)
