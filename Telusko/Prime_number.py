
##Here i values we are taking 2,3,4,5,6,7 to divide num, hence using i in range

num = int(input("Enter number: "))

for i in range(2,num):
    if num%i == 0:
        print(f"{num} is not a Prime Number")
        break
else:
    print(f"{num} is Prime Number")

