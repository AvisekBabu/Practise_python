
def myfunc():
    print("How are you")

myfunc()


# Parameterized function
def myfunc1(x, y):
    result = x+y
    print(result)


myfunc1(10,15)


# Suppose I want to store value in data base with object name result
# And later I will use that
def myfunc2(x, y):
    result = x+y
    return result



obj = myfunc2(10,16)
print(obj)


# Suppose I want to store two values, then need to accept two values
def myfunc3(x, y):
    result1 = x + y
    result2 = x - y
    return result1, result2


result1, result2 = myfunc3(10,15)
print(result1, result2)

# def myfunc3(x):
#     print(x)
#
# result1= myfunc3(108)
# print(result1)


