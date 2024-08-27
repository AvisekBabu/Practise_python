data = {1:'Car', 2:'Bike', 3:'Auto'}

print(data.get(1)) #Fetching key value
print(data[2]) #Fetching key value
print(data.get(4, "Not found")) #Fetching value and overighting if no value contains


#merging two list in one dictionary as a key and value
key = [1,3,5]
value = ['JAVA', 'PYTHON', 'JS']

# obj[7] = 'C++'

obj = dict(zip(key,value))


#We can add new value inside dic
obj[7] = 'C++'
print(obj)


#We can delete any key inside dictionary
del obj[3]
print(obj)

#Using sub dictionary to fetch data
multipleDic = {'PYTHON':['Pycharm','Sublime'], 'JS':'Atom', 'JAVA':{'JEE': 'Eclipse', 'JS': 'VSCode'}}

print(multipleDic['JS'])
print(multipleDic['PYTHON'][1])
print(multipleDic['JAVA']['JS'])
print(multipleDic.get('PYTHON'))
