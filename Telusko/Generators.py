# yield is generator which can gives iterator
# def topten():
#     # yield 5
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#
#
# values = topten()
# print("not from i range", values.__next__())
#
# for i in values:
#     print(i)


def toptensquare():
    n = 1
    while n <= 10:
        square = n * n
        yield square  #  yield will store the value but not stop the function like return
        n += 1


values = toptensquare()

for i in values:
    print(i)  # When i will ask for next value, yield will give value by increasing 1 until it goes to 10

"""
Why we used Generators instead of iterator?
--> Suppose in usecase you need to fetch 1000 of records, hence instead of storing all records yield will give 1 value
at a time based on call from i
"""
