#----------------------------
# Python Exception Handling
#----------------------------

# TOPIC : Python Exception Handling Using try, except and finally statement

"""
Exceptions in Python :
1. Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).
2. When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.

for eg.
For example, let us consider a program where we have a function A that calls function B, which in turn calls function C.
If an exception occurs in function C but is not handled in C, the exception passes to B and then to A.

If never handled, an error message is displayed and our program comes to a sudden unexpected halt.

Catching Exceptions in Python :
1. In Python, exceptions can be handled using a try statement.
2. The critical operation which can raise an exception is placed inside the 'try' clause.
   The code that handles the exceptions is written in the 'except' clause.

   We can thus choose what operations to perform once we have caught the exceptions.
"""

# The table below shows built-in exceptions that are usually raised in Python:
# ArithmeticError	      : Raised when an error occurs in numeric calculations
# AssertionError	      : Raised when an assert statement fails
# AttributeError	      : Raised when attribute reference or assignment fails
# Exception	              : Base class for all exceptions
# EOFError	              : Raised when the input() method hits an "end of file" condition (EOF)
# FloatingPointError	  : Raised when a floating point calculation fails
# GeneratorExit	          : Raised when a generator is closed (with the close() method)
# ImportError	          : Raised when an imported module does not exist
# IndentationError	      : Raised when indendation is not correct
# IndexError	          : Raised when an index of a sequence does not exist
# KeyError	              : Raised when a key does not exist in a dictionary
# KeyboardInterrupt	      : Raised when the user presses Ctrl+c, Ctrl+z or Delete
# LookupError	          : Raised when errors raised cant be found
# MemoryError	          : Raised when a program runs out of memory
# NameError	              : Raised when a variable does not exist
# NotImplementedError	  : Raised when an abstract method requires an inherited class to override the method
# OSError	              : Raised when a system related operation causes an error
# OverflowError	          : Raised when the result of a numeric calculation is too large
# ReferenceError	      : Raised when a weak reference object does not exist
# RuntimeError	          : Raised when an error occurs that do not belong to any specific expections
# StopIteration	          : Raised when the next() method of an iterator has no further values
# SyntaxError	          : Raised when a syntax error occurs
# TabError	              : Raised when indentation consists of tabs or spaces
# SystemError	          : Raised when a system error occurs
# SystemExit	          : Raised when the sys.exit() function is called
# TypeError	              : Raised when two different types are combined
# UnboundLocalError	      : Raised when a local variable is referenced before assignment
# UnicodeError	          : Raised when a unicode problem occurs
# UnicodeEncodeError	  : Raised when a unicode encoding problem occurs
# UnicodeDecodeError	  : Raised when a unicode decoding problem occurs
# UnicodeTranslateError	  : Raised when a unicode translation problem occurs
# ValueError	          : Raised when there is a wrong value in a specified data type
# ZeroDivisionError	      : Raised when the second operator in a division is zero


# Description : Here we will try to get a value form user which has to be Y/N. If it is something else we will generate exception
#               We can either have the process create an exception or we can raise an exception. Here we have raised an exception using 'raise' keyword: raise TypeError("Unsupported request :(")

try:
    user_choice = input("Do you want to continue ?. (Y/N) : ")
    if ((user_choice == 'Y') or (user_choice == 'y')):
        print("User wants to continue")
    elif ((user_choice == 'N') or (user_choice == 'n')):
        print("User does not want to continue")
    else:
        raise TypeError("Unsupported request :(")
except Exception as excp: # Here we are catching the exception in 'excp', this is not necessary tho. Only needed if you need to debug the type of exception.
    print("Exception generated :: ", excp)
    user_choice = input("Unsupported request ... Do you want to continue ?. (Y/N) :")

# NOTE : You can also put the above logic in a while loop and iterate till the user enters the correct value. for eq.

correct_choice = 0
while (correct_choice==0):
    try:
        user_choice = input("Do you want to continue ?. (Y/N) : ")
        if ((user_choice == 'Y') or (user_choice == 'y')):
            print("User wants to continue")
            correct_choice = 1
        elif ((user_choice == 'N') or (user_choice == 'n')):
            print("User does not want to continue")
            correct_choice = 1
        else:
            raise TypeError("Unsupported request :(")
    except Exception as excp:  # Here we are catching the exception in 'excp', this is not necessary tho. Only needed if you need to debug the type of exception.
        print("Exception generated :: ", excp)
        user_choice = "Unsupported request ... Please enter either : (Y/N) :"


# Catching Specific Exceptions in Python
# In the above example, we did not mention any specific exception in the except clause.
# This is not a good programming practice as it will catch all exceptions and handle every case in the same way. We can specify which exceptions an except clause should catch.
# NOTE : A try clause can have any number of except clauses to handle different exceptions, however, only one will be executed in case an exception occurs.
#        We can use a tuple of values to specify multiple exceptions in an except clause. Here is an example pseudo code.

try:
    user_choice = int(input("Please enter the typr of exception to raise (1/2/3) : "))

    if (user_choice == 1):
        print("Raising Exception 1")
        raise TypeError("Type1 Exception")
    elif (user_choice == 2):
        print("Raising Exception 2")
        raise NameError("Type2 Exception")
    elif (user_choice == 3):
        print("Raising Exception 3")
        raise ValueError("Type3 Exception")
except (TypeError, NameError) as excp: # Using one except block to catch two types of errors
    print("User has raised a Type 1/2 Exception : ", excp)

except (ValueError) as excp: # using another except block
    print("User has raised a Type 3 Exception : ", excp)

# 'try' with else clause
# In some situations, you might want to run a certain block of code if the code block inside try ran without any errors.
# For these cases, you can use the optional else keyword with the try statement.
#  NOTE : Exceptions in the else clause are not handled by the preceding except clauses.

# for eg : below is code that excepts only even numbers and prints does some operation if even number is entered. Otherwise Exception is raised.

try:
    input_val = int(input("Enter a number : "))
    assert input_val%2 == 0 , "Number not even"
except Exception as e:
    print("Encountered exception : ", e)
else:
    print("The number to the power 2 is :: ", pow(input_val, 2))

# 'finally' statement
#   1. The try statement in Python can have an optional finally clause. This clause is executed no matter what, and is generally used to release external resources.

# For example, we may be connected to a remote data center through the network or working with a file or a Graphical User Interface (GUI).
# In all these circumstances, we must clean up the resource before the program comes to a halt whether it successfully ran or not.
# These actions (closing a file, GUI or disconnecting from network) are performed in the finally clause to guarantee the execution.

# Here is an example of file operations to illustrate this.

# try:
#    f = open("test.txt",encoding = 'utf-8')
#    # perform file operations
# finally:
#    f.close()

# This type of construct makes sure that the file is closed even if an exception occurs during the program execution.