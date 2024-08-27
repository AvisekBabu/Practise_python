"""
With the help of decorators you can add extra features in existing functions
"""

# def div(a,b):
#     print(a/b)
#
# div(2,4)

#Suppose I want to swap large number first if user do mistakes

# def div(a,b):
#     if a<b:
#         a,b = b,a
#     print(a/b)
#
# div(2,4)

#Suppose div function defined in other file
"""
The updated_div function is a decorator that modifies the behavior of the div function.
The decorator ensures that the division is always performed with the larger number as the numerator.
"""

def div(a,b):
    print(a/b)

def updated_div(func):
    def inner_func(a,b):
        if a < b:
            a, b = b, a
        return func(a,b)
    return inner_func
    

final_div = updated_div(div)
final_div(2,4)

# div(3,5)

def parent_div(a, b):
    print(a / b)


def child_div(func):
    def inner_func(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner_func


user_input = child_div(parent_div)
user_input(5,25)