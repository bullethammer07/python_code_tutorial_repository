#--------------------
# Python Decorators
#--------------------

# Python has an interesting feature called decorators to add functionality to an existing code.
# This is also called 'metaprogramming' because a part of the program tries to modify another part of the program at compile time.

# Prerequisites for learning decorators :
# In order to understand about decorators, we must first know a few basic things in Python.
#
#   1. We must be comfortable with the fact that everything in Python (Yes! Even classes), are objects.
#   2. Names that we define are simply identifiers bound to these objects. Functions are no exceptions, they are objects too (with attributes).
#   3. Various different names can be bound to the same function object.

def first(msg):
    print(msg)

first("Hello")

second = first
second("Hello Ssup ?.")

# When you run the code, both functions first and second give the same output.
# Here, the names first and second refer to the same function object.

#----------------------------------------------------------------------------------------------------------------
# NOTE : Functions can be passed as arguments to another function.
# Such functions that take other functions as arguments are also called higher order functions. Here is an example of such a function.

print("\n")
def square_of_num(num):  # returns the square of a number
    return num**2

def cube_of_num(num):  # returns the cube of a number
    return num**3

def square_or_cube(func, num): # here a function has been passed as argument to this function, which is used inside the function.
    result = func(num)
    return result

print("passing square function : ", square_or_cube(square_of_num, 2))
print("passing cube function : ", square_or_cube(cube_of_num, 3))
