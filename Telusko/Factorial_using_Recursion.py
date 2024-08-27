
def factorialofrecursion(n):

    if n == 0:
        return 1

    return n*factorialofrecursion(n-1)


result = factorialofrecursion(5)
print(result)