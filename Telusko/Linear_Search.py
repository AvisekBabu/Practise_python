# arr = [5, 9, 2, 2, 1]
#
# for i in arr:
#     if i == 4:
#         print(i)
#         break
# else:
#     print("not present")

arr = [5, 9, 2, 4, 1]
n = 4

pos = -1

# def search(arr, n):
#     i = 0
#     while i < len(arr):
#         if arr[i] == n:
#             globals()['pos'] = i  # want to print the location and store as global
#             return True
#         i = i+1
#     return False
#
#
# if search(arr, n):
#     print("found at the position of", pos)
#
# else:
#     print("Not found")


def search(arr, n):
    for i in arr:
        if i == n:
            globals()['pos'] = i
            return True
    return False


if search(arr, n):
    print("found at the position of", pos)

else:
    print("Not found")