#Factorial of 5 is 120 = 1*2*3*4*5

def fact(x):
    f = 1
    """
    range(x) will start from 0 to 4
    Want to start from 1(started from 1) and finished at 5(given x+1)
    """
    for i in range(1,x+1):
        f = f*i

    return f

x = 5

result = fact(x)
print(result)