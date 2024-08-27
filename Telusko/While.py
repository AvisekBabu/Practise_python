
# x = 5
# while x >= 1:
#     print("Avisek", x)
#     x = x-1

#Restarted the i condition from start
count = 1
# j = 1
while count <=5:
    # print("Avisek", i)
    print("Avisek ", end="") #used end="" to print in same line "Avisek Win.."
    #Restarted the j condition from every each i condition
    j = 1
    while j <= 4:
        print("Win ", end="") #used end="" to print in same line "Win Win.."
        j = j+1
    count = count+1
    print() #Everytime i iteration should print in new line hence print() introduced


# Example of list iterating via while
fruits = ["Apple", "Bananna", "PineApple"]
# print(len(fruits))
index = 0
while index <= (len(fruits)):
    print(fruits[index])
    index = index-1

