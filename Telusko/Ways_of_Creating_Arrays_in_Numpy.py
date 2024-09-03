"""
Different types of creating arrays:
array()
linspace()
logspace()
arange()
zeros()
ones()

"""
from numpy import *

#   array()
# arr = array([1, 2, 3, 4, 5])
# arr = array([1, 2, 3, 4, 5.0])  #  By giving one value as float explicitly numpy will convert to float
# arr = array([1, 2, 3, 4, 5.0], int) #  in case I want to convert into a particular data type
arr = array([1, 2, 3, 4, 5], float)

print(arr.dtype)
print(arr)

#   linspace()
# arr1 = linspace(0, 16, 3) #  Data will be divided into 3 parts in float type
arr1 = linspace(0, 16, 20)  #  Data will be divided into 20 parts in float type
# arr1 = linspace(0, 15) #  if we don't mention parts value then arr1 will be divided in 50 parts

print(arr1)

#  arange()
arr2 = arange(0, 16, 3)  # Here 3 is like a step value between range of 0 to 16

print(arr2)

#  logspace()
#  First digit will be (ten rest to 1) 10^1, last one 10^40 and it will be divided into 5 parts
arr3 = logspace(0, 40, 5)

print(arr3)

#  zeros and ones will give all values as 0 or 1
arr4 = zeros(5)
arr5 = ones(5, int)  #  By default print output will be float, if I want to convert into integer

print(arr4)
print(arr5)
