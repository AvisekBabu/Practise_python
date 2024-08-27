from array import *

"""
array — typecode:
https://docs.python.org/3/library/array.html
signed int = values range starts from negative to positive
unsigned int = values range starts from negative to positive
"""


vals = array("i",[2,4,6,-8,9,3])


# print(vals)
# print(vals.buffer_info()) #address and size
# print(vals[0])
# print(vals.typecode)

#Different types of for loop works e.g. range()/(len(vals))/vals
# for j in range(6):
# for j in range(len(vals)):
#     print(vals[j])
# for j in vals:
#     print(j)

#Or we can use while loop as well
# j=0
# while j < (len(vals)):
#     print(vals[j])
#     j=j+1


#Exercise

newvals = array("u",['e','j','d','k'])


#Suppose above database I don't have access from which want to copy data
newArray = array(newvals.typecode,(a for a in newvals)) #a will fetch single values from newvals
# for x in newvals:
#     print(x)

x = 0
while x < len(newvals):
    print(newvals[x])
    x = x + 1
