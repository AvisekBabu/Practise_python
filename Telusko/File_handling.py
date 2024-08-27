"""Opening and reading the file"""
f = open("Data.txt", 'r')

# print(f.read())
print(f.readline(4))  # will print first 4 lines
#  Below code will print first two line
print(f.readline(), end='#')
print(f.readline())
#  will continue printing next lines if I add readline()
f.close()

"""Creating and writing a file"""

f1 = open("Data_new.txt", 'w')
# print(f1)
f1.write("Hi, Woman")
f1.write("How are you")
f1.close()

"""Appending new context in existing file"""

f3 = open("Data_new.txt", 'a')
f3.write("Hello")
f3.close()
f3 = open("Data_new.txt", 'r')
print(f3.read(), ",from f3")

"""Copying all Data.txt contexts to Data_new.txt"""

f = open("Data.txt", 'r')
f1 = open("Data_new.txt", 'w')

for data in f:
    # print(data, end='') #  will print all data
    f1.write(data)  # all the data which stored in f, will be written inside f1. And later in Data_new.txt

"""Copying .png file to another new file"""
#  We are using binary instead of characters in .png file
#  Hence need to give rb, wb where b stands for binary
f4 = open("9038613920.png", 'rb')
f5 = open("screenshot.png", 'wb')

for imagedata in f4:
    # print(f4)
    f5.write(imagedata)

# Need to learn import os
