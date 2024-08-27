# class University:
#     def colleges(self):
#         print("inside class method")
#
#     class College:
#         def kalyani_university(self):
#             print("inside inner class method")
#
#
# obj = University()
# obj.colleges()
#
# obj1 = University.College()
# obj1.kalyani_university()



class University:

    def __init__(self, name):
        self.name = name
    def colleges(self):
        print("inside class method & ", self.name)

    class College:

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def kalyani_university(self):
            print("inside inner class method & ", self.name, self.age)


obj = University("Parent_class")
obj.colleges()

obj1 = University.College("Child_class", 45)
obj1.kalyani_university()

