# PYTHON FUNCTION STRUCTURE :
# def function_name(parameters):
# 	"""docstring"""
# 	statement(s)

# Above shown is a function definition that consists of the following components.
#   1. Keyword def that marks the start of the function header.
#   2. A function name to uniquely identify the function. Function naming follows the same rules of writing identifiers in Python.
#   3. Parameters (arguments) through which we pass values to a function. They are optional.
#   4. A colon (:) to mark the end of the function header.
#   5. Optional documentation string (docstring) to describe what the function does.
#   6. One or more valid python statements that make up the function body. Statements must have the same indentation level (usually 4 spaces).
#   7. An optional return statement to return a value from the function.

# Docstrings :
#   1. The first string after the function header is called the docstring and is short for documentation string. It is briefly used to explain what a function does.
#   2. Although optional, documentation is a good programming practice. Unless you can remember what you had for dinner last week, always document your code.
#   3. We have a docstring immediately below the function header. We generally use triple quotes so that docstring can extend up to multiple lines.
#      This string is available to us as the __doc__ attribute of the function.

def system_info():
    """This function is used to print the system info"""
    print("Running Win 10")
    return 1

system_info()
# printing the function docstring
print(system_info.__doc__)

#-------------------------------------------------------------------
# making a simple function

def function1():
    print("You are inside function 1")

# calling the function
function1()

# printing the function1()
print(function1()) # This will return None as the function does not have a return type

#-------------------------------------------------------------------
# making a simple function with a return type

print("\n")

def function2():
    print("You are inside function 2")
    return "Function Completed"

# calling the function
function2()
# printing the function1()
print(function2())

#-------------------------------------------------------------------
# passing inputs and parameters to a function

def add_func(a, b):
    print("The sum is : ", a+b)

add_func(6, 4)


