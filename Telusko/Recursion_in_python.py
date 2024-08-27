import sys

sys.getrecursionlimit()

#We can set recursion limit
sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())

i = 0
def Rec():
    global i
    i = i + 1
    print("Hello ", i)
    Rec()

Rec()