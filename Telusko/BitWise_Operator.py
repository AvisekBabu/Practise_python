"""
Complement (~)
And (&)
Or (|)
XOR (^)
Left Shift (<<)
Right Shift (>>)
"""

# Complement (~)
# Binary format of 13 is 00001101
# one's complement of 13 is 11110010
# two's complement formula is (one's complement + 1)
# two's complement of 13 is 11110010+1 = 11110011
# So two's complement of 13 is -13(binary format of -13 is 11110011)

num = (~12)
print(num)


# And (&)
# 12 binary format = 00001100
# 13 binary format = 00001101
# for BitWise "&" case, at last 0 from 12 and 1 from 13 will be 0
# So the value will be 00001100 which is 12

num1 = 12 & 13
print(num1)


# Or (|)
# 12 binary format = 00001100
# 13 binary format = 00001101
# for BitWise "|" case, at last 0 from 12 and 1 from 13 will be 1
# So the value will be 00001100 which is 13

num2 = 12 | 13
print(num2)


#XOR (^)
# Sequence of XOR
# 0 0 = 0
# 0 1 = 1
# 1 0 = 1
# 1 1 = 0
# 12 binary format = 00001100
# 13 binary format = 00001101
# XOR format ======= 00000001 which is 1

num3 = 12^13
print(num3)


# Left Shift (<<)
# 12 binary = 00001100
# Left shifted means 00110000 where two zero's added at last from 00001100.00
# Every number having .0000
# decimal value of 110000 is 48
num4 = (12<<2)
print(num4)

# Right Shift (>>)
# Same concept as above but will right shift
# 12 = 00001100, after shifting 00000011
# decimal value of 00000011 is 3
num5 = (12>>2)
print(num5)
