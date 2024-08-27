"""
We define one function which doesn't have a name called Anonymous_Function,
with help of lambda
Use lambda when there should be one expression on return
"""

# def square(x):
#     return x * x
#
# result = square(5)
# print(result)

# def test():
#     print("hello")
#
# test()

test = lambda : print("Hello World")

test()

f = lambda x:x * x

result = f(5)
print(result)

#lambda with two argument
doublearg = lambda x, y:x+y

result1 = doublearg(5,6)
print(result1)