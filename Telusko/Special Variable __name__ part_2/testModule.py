# Define my functions in module
def add(a,b):
    print("Sum of two number")


def sub():
    print("Substraction of two number")


# Encapsulating all functions inside main function
# So main() will work as a common function
def main():
    add(5,6)
    sub()

# main() #if I don't define main() with condition then all files related to this module will print in actual_file.py

if __name__ == "__main__":
    main()

