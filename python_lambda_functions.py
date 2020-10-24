# Python Lambda Functions.

# What are lambda functions in Python?
# In Python, an anonymous function is a function that is defined without a name.
# While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.
# Hence, anonymous functions are also called lambda functions.

# Syntax : lambda arguments: expression

# NOTE : Lambda functions can have any number of arguments but only one expression.
#        The expression is evaluated and returned.
#        Lambda functions can be used wherever function objects are required.

# Example 1

val = lambda x: x**2
print("4 power 2 is : ", val(4))

# The statement : double = lambda x: x * 2
# is nearly the same as:
# def double(x):
#    return x * 2

# Use of Lambda Function in python :
# We use lambda functions when we require a nameless function for a short period of time.
# In Python, we generally use it as an argument to a higher-order function (a function that takes in other functions as arguments).
# Lambda functions are used along with built-in functions like filter(), map() etc.

# Example use with filter() :
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)

# Example use with filter() :
# Program to double each item in a list using map()

new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)