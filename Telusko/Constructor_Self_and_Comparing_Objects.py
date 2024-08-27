class Computer:
    #static intances
    def __init__(self):
        self.name = "Avisek"
        self.age = 32

    #modifying instances with custom method
    def update(self):
        self.name = "Unknown"

    #Custome method defined for comparison
    def compare(self, c2):
        if c1.age == c2.age:
            return True
        else:
            return False

#Creating the object in heap
c1 = Computer()
c2 = Computer()

#Changed c1.name & c1.age value
#At this point c1 and c2 having same instance with different value
c1.name = "Animesh"
c1.age = 24

# c1.update()#in this self will re-direct the correct instance value which is c1.name="Unknown" not c2.name="Avisek"
# Assignment e.g. c1 -> update() -> self -> name -> get updated value "Unknown" -> assign back to c1

#We can compare both object
if c1.compare(c2):
    print("Both having same age")
else:
    print("Different age")

# print(id(c1))
print(c1.name)


