"""
We can merge two tuples/set/dict/list by zip and later migrate them into list/set/dict/tuple for iterate
"""

names = ("Avisek", "Jitu", "Sandeep", "Jitu")
# names = ["Avisek", "Jitu", "Sandeep", "Jitu"]
company = ("Innominds", "RNS", "Cognigent", "QC")
# print(type(company))

zipped = list(zip(names, company))
# zipped = set(zip(names, company))
# zipped = dict(zip(names, company))
# zipped = tuple(zip(names, company))

print(zipped)

for (a, b) in zipped:
    print(a, b)
