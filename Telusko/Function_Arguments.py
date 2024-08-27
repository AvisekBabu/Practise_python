
#1, below x having different memory hence 10 will not make effect
# def update(x):
#     x = 8
#     print(x)
#
# update(10)

# def update(x):
#     x = 8
#     # print(x)
#     print("x", x) #Different value
#
# a = 10
# update(a)
# print("a", a) #Different value

#Below address will be same as we are sending reference
def update(x):
    print(id(x)) # id in memory is 140722328115928, same as a
    x = 8
    print(id(x)) # The moment I change value then memory address will be changed e.g. 140722328115864
    # print(x)
    print("x", x)

a = 10
update(a)
print("a", a)
print(id(a)) # id in memory is 140722328115928, same as x

#Lets try with a list, which is mutable hence modifying second value
def updatelist(mylist):
    print(id(mylist))
    mylist[1] = 78
    print(mylist)


mylist = [25, 34, 67]
updatelist(mylist)
print(id(mylist))

