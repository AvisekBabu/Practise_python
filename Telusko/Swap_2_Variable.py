a = 5
b = 6

"""
We can swap a to b and b to a with three ways
1. Using third variable
2. Using formula
3. Using XOR formula
4. Using python unique technique
"""

# 1. Using third variable

# thirdVariable = a
# a = b
# b = thirdVariable
# print(a)
# print(b)

# 2. Using formula
# a = a + b
# b = a - b
# a = a - b
# print(a)
# print(b)


# 3. Using XOR formula
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print(a)
# print(b)

# 4. Using python unique technique
a,b = b,a
print(a)
print(b)