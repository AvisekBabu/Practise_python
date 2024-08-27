
class Computer:
    #Here __init__ works as constructor
    #it will take argument from main object com1=Computer() and assign to local object
    def __init__(self, gen, ram, rom):
        self.gen = gen
        self.ram = ram
        self.rom = rom

    #this method work as returning or printing object value
    #Similar like getters and setters, getters for this case
    def config(self):
        # print("Computer having ", self.gen, self.ram, self.rom)
        configset = f"Computer having {self.gen},{self.ram},{self.rom}"
        print(configset)



#Main method from where need to pass arguments
com1 = Computer('i5', '4GB', '500GB')
com2 = Computer('i7', '8GB', '1TB')

#finally calling the main method
com1.config()
com2.config()
# print(com1.gen)





