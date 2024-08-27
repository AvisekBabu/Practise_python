"""
if I run this Demo file then __name__ will be print __main__, as it is the main file
But if I import this Demo.py as module in different file then __name__ will print module name "Demo" along
with all other code which belongs to this Demo.py
"""

print(__name__)
# print("inside Demo")

"""
But make sure all files are under function and function defined with condition,
else all print statement will be printed there.
print(__name__) is optional.
"""

def main():
    print("inside Demo")

if __name__ == "__main__":
    main()