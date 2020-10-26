# -------------------------------
# *args and **kwargs in Python
# -------------------------------

# In Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols:
# 1.)*args (Non-Key Arguments)
# 2.)**kwargs (Key word Arguments)

# “We use *args and **kwargs as an argument when we have no doubt about the number of  arguments we should pass in a function.”

# Example 1 : Using *args

def my_function1(*args_1):
    print("This is inside function for *args")
    for val in args_1:
        print("Name is :: ", val)


names = ["Jayant", "Nikhil", "Mohit", "Parveen", "Amit"]  # This is a list
# This provides a convenience as :
# Now you can add as many items to the list/iterable without having to worry about the number of arguments
# to be passed in the function.
my_function1(*names)  # NOTE : Even tho 'names' is a list, however *args always get passed on a tuple.


# Example 2 : Passing normal/regular arguments along with *args
# NOTE : The ordering in which arguments are passed in thefunction, normal/regular arguments take precedence over *args and **kwargs
#        if this ordering is not followed, an error is returned.
#        Thus, declare normal/regular arguments before *args or **kwargs

def my_function2(val1, *args_1):  # NOTE : If the arguments were passed as (*args_1, val1) instead of (val1, *args_1), It will return with an Error
    print("The regular argument passed is : ", val1)

    for val in args_1:
        print("Name is :: ", val)


my_function2("random arg", *names)
