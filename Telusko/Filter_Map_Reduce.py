
# def is_displayed(n):
#     return n%2 == 0
#
# nums = [3,5,6,9,34,23,56]
#
# evens = list(filter(is_displayed, nums))
# print(evens)


#Using lambda

nums = [3,5,6,9,34,23,56]

evens = list(filter(lambda n:n%2==0, nums))
print(evens)

doubles = list(map(lambda n:n*2, evens))
print(doubles)

from functools import reduce

# def add_all(a,b):
#     return a+b
# add_all(4,5)
sum = reduce(lambda a,b:a+b, doubles)
print(sum)
