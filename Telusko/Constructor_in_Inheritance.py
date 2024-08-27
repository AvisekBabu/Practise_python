# class A:
#     def __init__(self):
#         print("init from class A")
#
#     def feature1(self):
#         print("Hello from feature1")
#
# """
# With super().__init__ keyword we can enter into parent class default constructor
# Then again compiler will come to class B __init__ and print "init from class B"
# """
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("init from class B")
#
#     def feature2(self):
#         print("Hello from feature2")


# f2 = B()


"""
What if class C having two parent-class class A & class B
In this case, as per MRO[METHOD RESOLUTION ORDER] C(B,A) B will be called first
"""
# class A:
#     def __init__(self):
#         print("init from class A")
#
#     def feature1(self):
#         print("Hello from feature1")
#
#
# class B:
#     def __init__(self):
#         print("init from class B")
#
#     def feature2(self):
#         print("Hello from feature2")
#
#
# #as per MRO from C(B,A), B will be called first
# class C(B, A):
#     def __init__(self):
#         super().__init__()
#         print("init from class C")
#
#     def feature3(self):
#         print("Hello from feature3")
#
#
#
# f2 = C()


"""
What if parent-classes class A & class B having same methods feature1
In this case, as per MRO[METHOD RESOLUTION ORDER] C(B,A) B feature1 will be called first
"""
class A:
    def __init__(self):
        print("init from class A")

    def feature1(self):
        print("Hello from <class A - feature1>")

    def feature2(self):
        print("Hello from feature2")


class B:
    def __init__(self):
        print("init from class B")

    def feature1(self):
        print("Hello from <class B - feature1>")


#In below inheritance(B, A) if anything not found in B then compiler will go to A
#as per MRO from C(B,A), B feature1 will be called first
class C(B, A):
    def __init__(self):
        super().__init__()
        print("init from class C")

    def feature3(self):
        print("Hello from feature3")

    #We can call any parent class method by super
    def calling_parent_method(self):
        super().feature2()



f2 = C()

f2.feature1()

f2.feature2() #calling parent class method
