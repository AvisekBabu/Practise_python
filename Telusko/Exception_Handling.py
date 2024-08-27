"""
Suppose b=h then compiler will go to ValueError exception, as we are taking input as integer
Suppose k=h then compiler will go to ValueError exception
Suppose b=0 then compiler will go to ZeroDivisionError exception, as we 0 can't be divided
Suppose I am not aware of type of error then it will fall under Exception block
"""

a = 10
# b = int(input("Enter division number-"))

try:
    b = int(input("Enter division number-"))
    print("resource open")
    print(a/b)
    k = int(input("Enter a number-"))
    print(k)
    # print("resource close")

except ValueError as e:
    print("Can't give other data types except integer:", e)

except ZeroDivisionError as e:
    print("Can't divide by zero:", e)
#  Catch the exception inside except block
#  Don't close or stop anything inside try or except block
except Exception as e:
    print("Bye", e)
#  finally block will execute both conditions
#  if you get exception or without exception
finally:
    print("resource close")
