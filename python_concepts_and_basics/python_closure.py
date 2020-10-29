#-----------------
# Python Closure
#-----------------

# Defining a closure function :
# In this arrangement, the function itself returns a function.

# Making a top function
def top_function(num):

    # making a nested function
    def nest_func1():
        for val in range(int(num)):
            print(val)

    return nest_func1

# The 'top_function' was called with the argument '10' and the returned function was bound to the name 'copy_func'
copy_func = top_function(10)

# On calling 'copy_func' the message will still be remembered although we have already finshed executing 'top_function'
copy_func()

# This technique by which some data ('10' in this case) gets attached to the code is called closure in Python.

# now even if we delete the functon 'top_function', the copy_func() will still retain the output
print("\n")
del top_function
copy_func()

#--------------------------------------------------------------------------------------------------------------------------
# When to use closures?
# So what are closures good for?

#   1. Closures can avoid the use of global values and provides some form of data hiding. It can also provide an object oriented solution to the problem.
#   2. When there are few methods (one method in most cases) to be implemented in a class, closures can provide an alternate and more elegant solution.
#      But when the number of attributes and methods get larger, it's better to implement a class.
#   3. Python Decorators make an extensive use of closures.

# NOTE : All function objects have a __closure__ attribute that returns a tuple of cell objects if it is a closure function.
#        Referring to the example above, we know 'copy_func' is a closure functions.

print("\n")
print("printing the closure attribute : ", copy_func.__closure__)

# The cell object has the attribute cell_contents which stores the closed value.
print("closure attribute contents : ", copy_func.__closure__[0].cell_contents) # This will return 10