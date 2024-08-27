
new_arr = sorted([56, 90, 56, 798, 345, 98])

n = 345

pos = -1

def binary_search(new_arr, n):
    lower_bound = 0
    upper_bound = len(new_arr)-1

    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound) // 2  # //2 to get int value or we will get 2.5

        if new_arr[mid] == n:  # we will catch the value into this by ranging the list shroter
            globals()['pos'] = mid
            return True
        else:
            #  Shorter the lower bound value by iterating below condition
            if new_arr[mid] < n:
                lower_bound = mid
            else:
                upper_bound = mid
    return False


if binary_search(new_arr, n):
    print("found at ", pos)
else:
    print("Not found")
