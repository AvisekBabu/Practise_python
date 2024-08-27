"""
When we are working with operator overloading we are working with default constructors behind the scene
Hence if we are returning something by comparing two objects arguments which are associated with same class,
Then we need to use default methods/constructor like below.
Because int + int / methods knows operator of + but class don't know
"""
# a = 89
# b = 67
#
# # print(a+b)
# print(int.__add__(a,b)) # a+b in back calling __add__ constructor
# print(str.__add__(a,b))

class Student:
    def __init__(self, m1, m2):  # default constructor which will take two argument
        self.m1 = m1
        self.m2 = m2

    """Defining different different operators constructor to return result between 
    two or more(need to try *kwargs) arguments of class, need to practise more"""

    def __add__(self, other):  # self will accept m1 & other will accept m2 value
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)  # Logic of "int.__add__(a,b)" method
        return s3

    def __gt__(self, other):  # This is for greater than value
        r1 = self.m1 + other.m1
        r2 = self.m1 + other.m1
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):  # This is for converting string format
        # return self.m1, self.m2  # It should return string type as constructor is __str__
        return '{} {}'.format(self.m1, self.m2)  # Now it will return string


s1 = Student(23, 45)
s2 = Student(34, 89)

s3 = s1 + s2  # With + sign we are overloading operators here, as class Student not aware of "add" method hence we are implementing __add__(a,b)
print(s3.m1)  # printing the value of m1 marks

#Default constructor can't be called, below is not correct
# s1.m1()
# s2.m2()

if s1 > s2:  # With > sign we are overloading operators here, as class Student not aware of "greater than" method hence we are implementing __gt__(a,b)
    print("s1 Student is Higher")
else:
    print("s2 Student is Higher")






"""Suppose I want to print the value of a class variable"""
print(s1)  # It will give value <__main__.Student object at 0x0000021F4F64F8F0>, hence need to define function __str__

a = 5
print(a)  # It will print value of 5 as in backend (a.__str__()) will work, which will print string value
print(a.__str__())