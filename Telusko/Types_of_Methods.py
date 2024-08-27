"""
Instance methods
Class methods
Static methods
"""

class Student:
    University = "WBUT"

    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    """
    result is a "instance method" as we passed self, which dependent upon object to call e.g. obj1.result
    """
    def result(self):
        # return f"Marks are {self.marks1} , {self.marks2} , {self.marks3}"
        # totalResult = f"Marks are {self.marks1} , {self.marks2} , {self.marks3}"
        # print(totalResult)
        return (self.marks1 + self.marks2 + self.marks3)/3

    """get_student is a "class method" as we pass cls and annotation od @classmethod"""
    @classmethod
    def get_student(cls):
        return cls.University


"""get_info is a "static method" as we pass no argument and annotation od @staticmethod"""
    @staticmethod
    def get_info():
        print("inside static method")


    """
    We have Accessor method & Mutator method.
    Accessor = for fetching the value, similar like Getters in java
    Mutator = for changing the value, similar like Setters in java
    """
    def set_result(self, new_marks1):
        self.marks1 = new_marks1

    def get_result(self):
        f"new marks is {self.marks1}"


obj1 = Student(23,67,89)
obj2 = Student(45,34,56)

"""
Modifying the value of a instance method
"""
obj1.set_result(99)

#Calling instance method
print(obj1.result()) #if we are returning in instance method
# obj1.result() #if we are printing in instance method

#Calling class method
print(Student.get_student())

#Calling static method
Student.get_info()