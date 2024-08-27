nums = [23,46,89,34,78]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    # continue
    print("Not found")
#While using for else we can move else one left intendetion
#So "Not found will not print each time"


