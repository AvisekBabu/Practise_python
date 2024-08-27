
def short(nums):
    for i in range(len(nums)):
        pos_min = i
        for j in range(i, len(nums)):
            if nums[j] < nums[pos_min]:
                pos_min = j
        # below everytime nums[i] value will be reassigned which will be stored in nums[pos_min]
        temp = nums[i]
        nums[i] = nums[pos_min]
        nums[pos_min] = temp
        # print(nums)

nums = [8, 3, 7, 2, 9, 5]
short(nums)
print(nums)