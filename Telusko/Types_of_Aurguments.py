"""
Actual Argument
 1. Position
 2. Keyword
 3. Default
 4. Variable length
"""


# Position argument: Where we have to give actual argument in proper sequence, else e.g.
# If I try to do print(age-5) it will throw error

# def person(name , age): #Formal Argument
#     print(name)
#     print(age)

# person("Abisek" , 25) #Actual Argument


# Keyword argument : If suppose function defined in other class
# which I don't have access but know what are arguments, then we don't have to maintain sequence

# def person1(name , age): #Formal Argument
#     print(name)
#     print(age)
#
# person1(age = 30, name = "Avisek")


# Default argument

# def person2(name, age=18):
#     print(name)
#     print(age)

# person2(name="Avi") #It will take age as default argument 18 if we not passing value
# person2("Avi",20)

# Variable length
# By giving *b from second argument all values will be taken as tuple
# def sum(a, *b):
#     print(a)
#     print(b)
#
# sum(34, 78, 89, 32)


def sumy(a, *b):
    c = a
    for i in b:
        c = c + i

    print(c)

sumy(34, 78, 89, 32)

#Lets take total arguments inside *b, it will shorter the above code with same result
# def sum(*b):
#     c = 0
#     for i in b:
#         c = c + i
#
#     print(c)
#
# sum(34, 78, 89, 32)

