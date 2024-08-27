from array import *

#Making structure of variable based on assumtion of user input
arr = array('i', [])

#Taking the length of array
User = int(input("Enter the length of array: "))

#Iterate each values of length & later appening one by one
for x in range(User):
    y = int(input("Enter next value: "))
    arr.append(y)

print(arr)

#If user want to know the index of his value
Val = int(input("Enter the value for search: "))

#Method1, we can find the index number
# print(arr.index(Val))

#Method2, we can find the index number
k = 0 #Giving counter variable, 'k' will work as indexing range of arr

for a in arr:
    if a == Val:
        print(k)
        break

    k+=1

