# Avail = 6
#
# x = int(input("How many you want?\n"))
#
# i = 1
#
# while i <= x:
#     #if x value is more then Avail then it will print "Out of order"
#     if x > Avail:
#         print("Out of order")
#         break
#     print("Available")
#     i+=1

"""
Continue Statement:
If the condition is True (i.e., i is divisible by 3 or 5), the continue statement is executed.
When continue is executed, the current iteration is skipped, and the loop moves to the next iteration.
The print(i) statement is not executed for this iteration.
"""

# for i in range(1,101):
#     #It will remove digit which divisible by 3 or 5
#     if i%3==0 or i%5==0:
#         continue
#         # pass
#     print(i)


"""
Purpose of pass:
The pass keyword is useful in situations where you have not yet 
decided what code to execute inside a loop or a conditional statement, 
but you want to maintain a syntactically correct structure.
"""

# for i in range(1,101):
#     #This will ignore odd number
#     if i%2!=0:
#         #Don't know actually what to include hence kept pass, later will add
#         pass
#     else:
#         print(i)


'''Difference between continue | Break | Pass'''
# for i in range(6):
#     if i==3:
#         #continue will go to 3 and not execute, it will go for 4
#         # continue
#         #break will stop print when 3 will come
#         # break
#         #pass will not execute anything under this if condition, pass will skip the block
#         #pass mainly used in function, where you will add any data & implement the function
#         # pass
#     print(i)


# def func():
#     pass
# func()