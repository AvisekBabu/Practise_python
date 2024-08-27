""" Difference of Local and Global variable"""
# a = 23
#
# def myfunc():
#     # a = 98 #func always prefer local, but if local not available then it will go with global variable
#     print("inside func", a)
#
# myfunc()
# print("Outside func", a)



""" Introduce of global variable"""
# x = 23
#
# def something():
#     global x
#     #if we mentioned global then inside local variable will convert to global
#     x = 45
#     print("inside func", x)
#
# something()
# print("Outside func", x)


"""Using globals(), explicitly we can call global variable along with local variables inside function"""

y = 23
z = 67


def something():
    y = 45 #suppose I want to keep local variable inside func environment
    print("inside func", y)
    j = globals()["y"] #using globals() explicitly we can call global variable
    # print(id(j))
    print("inside func of func", j)
    globals()["y"] = 39 #if you want to change global variable without effecting local variable

something()
print("Outside func", y)
# print(id(y)) #id(j) and id(y) both having same address in heap memory