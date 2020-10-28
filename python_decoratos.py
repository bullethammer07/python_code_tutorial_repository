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

#----------------------------------------------------------------------------------------------------------------
# NOTE : Furthermore, functions can also return another function.

# here 'returning_func' is a nested function which is defines and returned each time we call 'calling_func'
def calling_func(num):

    def returning_func():
        return num + 2

    return returning_func

new = calling_func(5)
print(new())

#----------------------------------------------------------------------------------------------------------------
# DECORATORS :
#   Functions and methods are called callable as they can be called.
#   In fact, any object which implements the special __call__() method is termed callable.
#   NOTE : So, in the most basic sense, a decorator is a callable that returns a callable.
#          Basically, a decorator takes in a function, adds some functionality and returns it.

print("\n")

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

# lets decorate this ordinary function
decorated_func = make_pretty(ordinary)
# calling the decorated function
decorated_func()

# In the example shown above, decorated_func() is a decorator. In the assignment step:
# decorated_func = make_pretty(ordinary)

# NOTE : Generally, we decorate a function and reassign it as :
# ordinary = make_pretty(ordinary)

# This is a common construct and for this reason, Python has a syntax to simplify this.
# We can use the @ symbol along with the name of the decorator function and place it above the definition of the function to be decorated. For example,

# @make_pretty
# def ordinary():
#     print("I am ordinary")
# is equivalent to

# def ordinary():
#     print("I am ordinary")
# ordinary = make_pretty(ordinary)

#----------------------------------------------------------------------------------------------------------------
# Decorating functions with parameters :

def modified_sum(func):

    def inner(x, y):
        return func(x, (y+3))

    return inner

# sum_of_sums gets modified from here
@modified_sum
def sum_of_nums(a, b):
    sum = a + b
    return sum

print(sum_of_nums(1, 2))

# NOTE : notice that parameters of the nested inner() function inside the decorator is the same as the parameters of functions it decorates.
# Taking this into account, now we can make general decorators that work with any number of parameters.
# we can use *args and **kwargs to take as many number of arguments.


