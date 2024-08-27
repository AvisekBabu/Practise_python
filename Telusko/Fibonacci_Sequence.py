"""
0 1 1 2 3 5 8 13 21 34...
"""

def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n <= 0:
        print("invalid number")
    else:
        print(a)
        print(b)

        # count_new = (count + b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
            #If I don't want to show more than 89
            if c >= 89:
                break
            else:
                continue

fib(30)