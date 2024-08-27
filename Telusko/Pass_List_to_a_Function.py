# def myfunc3(x, y):
#     result1 = x + y
#     result2 = x - y
#     return result1, result2
#
#
# result1, result2 = myfunc3(10,15)
# print(result1, result2)


# myList = [34 , 87 , 45 , 67 , 56]
# def myfunc(myList):
#     even = 0
#     odd = 0
#
#     for i in myList:
#         if i%2 == 0:
#             even = even+1
#         else:
#             odd = odd+1
#     return even, odd
#
# even , odd = myfunc(myList)
# # print(even,odd)
# print("Even : {} and Odd : {}".format(even, odd)) #format() belongs to a String
# print("count of even number: ", even)
# print("count of odd number: ", odd)

"""
Assignment:
Takes multiple names from user and display the users who having length more than 5 letters
"""

Students = ["ugugfiur","gdtr","ugiufgeiuf","gf","ugeug"]
# Students = input("Enter name: ")

def morethanfive(Students):
    for i in Students:
        # print(i)
        # print(len(i))
        if len(i)>5:
            print(i)
        else:
            continue

morethanfive(Students)
