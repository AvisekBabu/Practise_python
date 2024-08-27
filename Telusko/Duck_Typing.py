class PyCharm:
    def execute(self):
        print("Python editor")


class VSCode:
    def execute(self):
        print("Java editor")


class Laptop:
    def config(self, ide):
        ide.execute()

ide = VSCode() # This condition will help to duck recognisation

avi = Laptop()
avi.config() #We are passing execute() method by ducking another execute() method