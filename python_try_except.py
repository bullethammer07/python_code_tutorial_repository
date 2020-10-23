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

   We can thus choose what operations to perform once we have caught the exception.

"""

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

