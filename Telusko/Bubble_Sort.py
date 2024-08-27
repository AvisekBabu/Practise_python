# i will handle the range of nums, i will work as outer loop by shortening list length
# j will handle the positional value of nums list, it will work as length define by i

def short(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp



nums = [8, 3, 7, 2, 9, 5]
short(nums)
print(nums)
