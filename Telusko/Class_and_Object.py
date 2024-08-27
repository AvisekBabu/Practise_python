class Computer:
    def config(self):
        print('i5', '4GB', '1TB')

# com1 is a constructor of Computer
com1 = Computer()
# com2 = Computer()

# We can call with two ways
#1. call with ref object of class
com1.config()
# com2.config()
#Or, 2. call with class itself by passing the object argument
Computer.config(com1)
# print(type(com1))
