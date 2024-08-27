# nums = [4, 6, 8, 7]
#
# # print(nums[0])
#
# it = iter(nums)
# print(it.__next__())
# # print(it.__next__())
#
# print(next(it))
# print(next(it))

class Topten:
    #  Defined the function for initial value
    def __init__(self):
        self.num = 1

    #  __iter__ method will iterate all the integer values
    def __iter__(self):
        return self

    #  __next__ method will capture the values one by one
    def __next__(self):
        #  loop will capture the run time value of self.num
        if self.num <= 10:
            loop = self.num
            self.num += 1
            return loop
        #  Need to define else for Stop the iteration
        else:
            raise StopIteration


obj = Topten()

#  Once 1 will be printed from below, 1 will not print from i range
print("not from i range", next(obj))

#  returned loop value will be iterate with i
for i in obj:
    print(i)

"""
__init__ Method: self.num = 1: This line sets the initial value of self.num to 1. This variable will 
keep track of the current number in the iteration.
Iteration: The for i in obj: loop begins iterating over obj.
The __iter__() method is called, which returns the object itself.
The loop then repeatedly calls the __next__() method to get the next value.
For each iteration, i takes the value returned by __next__() and print(i) outputs it.
This continues until __next__() raises a StopIteration exception (when self.num exceeds 10), at which point the loop stops.
"""