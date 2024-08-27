# Tupple is unmutable
tup = (67,89,67,45)
print(tup)
print(tup[2])
print(tup.index(67))

# Set will remove duplicate value
setExample = {24,78,56,98,78}
print(setExample)
# print(setExample[0]) //Can't indexing'
# setExample.remove(1)
setExample.add(57)
print(setExample)
