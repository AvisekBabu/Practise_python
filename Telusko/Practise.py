"""
Method overloading:
class Student:
    def marks(a,b)
    def marks(a,b,c)
---------------------
Method overriding:
Class Student:
    def marks(a,b)

Class NewStudent(Student):
    def marks(a,b)

"""


class Student:
    # def __init__(self, m1, m2):
    #     self.m1 = m1
    #     self.m2 = m2

    def sum(self, a, b, c):
        return a + b + c
        # return x

    def advsum(self, x=None, y=None, z=None): # Defined with =None, so if there is no overriding/ argument then it will not store anything
        s = 0
        if x != None and y != None and z != None:
            s = x + y + z
        elif x != None and y != None:
            s = x + y
        else:
            s = x
        return s


# s1 = Student(78, 45)

s1 = Student()
print(s1.sum(54, 56, 89))
# result = s1.sum(34, 67, 90)
# print(result)

print(s1.advsum(56, 78, 89))
print(s1.advsum(56, 78))  #  Now it will take two argument as we defined the function to accept two or one


"""Method overriding"""

class Calc:
    def show(self):
        print("inside Calc")


class AdvCalc(Calc):  # When nothing will be found inside AdvCalc then it will go inside Calc
    pass
    # def show(self):
    #     print("inside AdvCalc")




calculator = AdvCalc()
calculator.show()




