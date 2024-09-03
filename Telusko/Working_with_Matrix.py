from numpy import *

arr1 = array([
    (1, 4, 8, 4),
    (9, 7, 3, 9)
])

# print(arr1)
# print(arr1.dtype) #  will get the data type e.g. int
# print(arr1.ndim) #  number of rows
# print(arr1.shape) #  number of rows and columns


arr2 = array([
    (9, 5, 2, 7, 8, 9),
    (59, 34, 86, 84, 0, 64)
])

# arr3 = arr2.flatten() # it will merge two rows of arrays
# arr3 = arr2.reshape(3, 4)
arr3 = arr2.reshape(2, 2, 3) # [2D array[2 rows[3 columns][]] [[][]]]

print(arr3)


# a = int(input("first floor: "))
# b = int(input("first floor: "))
# c = int(input("first floor: "))
#
# x = int(input("second floor: "))
# y = int(input("second floor: "))
# z = int(input("second floor: "))

# arr4 = array([a,b,c,x,y,z])
arr4 = matrix("34, 23, 56, 12, 54, 78")
arr5 = matrix("43, 67, 98, 97, 34, 34")

m = arr4 + arr5

print(arr4)
print(m)