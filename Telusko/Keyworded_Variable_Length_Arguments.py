#Need to give two star ** if having keyword argument, instead of positional args..
def myAdd(name , **other_details):
    print(name)
    print(other_details)


# myAdd("Avisek",31, "Delhi", "700031")
myAdd("Avisek",age = 31, State = "Delhi", PinCode = "700031")

#iterating the **kwargs
def myDetails(nickname , **kwargs):
    print(nickname)
    # print(kwargs)
    for i,j in kwargs.items(): #To get key and value we need to give i,j
        print(i,j)

myDetails("Avi", age=32 , State = "WB" , Pin = 700051)