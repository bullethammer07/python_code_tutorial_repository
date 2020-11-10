#---------------------------------------
#          Python Co-Routines           
#---------------------------------------

# NOTE : An understanding of Python Generators is recommended before understanding coroutines.

# We all are familiar with function which is also known as a subroutine, procedure, subprocess etc.
# Subroutines in Python are called by main function which is responsible for coordination the use of these subroutines.
# NOTE : Subroutines have single entry point.

# Coroutines :
#----------------
# Coroutines are generalization of subroutines. They are used for cooperative multitasking where a process voluntarily 
# yield (give away) control periodically or when idle in order to enable multiple applications to be run simultaneously. 

# The difference between coroutine and subroutine is :
#   1. Unlike subroutines, coroutines have many entry points for suspending and resuming execution. 
#      Coroutine can suspend its execution and transfer control to other coroutine and can resume again execution from the point it left off.
#   2. Unlike subroutines, there is no main function to call coroutines in particular order and coordinate the results. 
#      Coroutines are cooperative that means they link together to form a pipeline. 
#   3. One coroutine may consume input data and send it to other which process it. Finally there may be a coroutine to display result.

# IMPT NOTE : Now you might be thinking how coroutine is different from threads, both seems to do same job.
#             In case of threads, it’s operating system (or run time environment) that switches between threads according to the scheduler. 
#             While in case of coroutine, it’s the programmer and programming language which decides when to switch coroutines. 
#             Coroutines work cooperatively multi task by suspending and resuming at set points by programmer.

# Python Coroutine :
#--------------------
# In Python, coroutines are similar to generators but with few extra methods and slight change in how we use yield statement. 
# Generators produce data for iteration while coroutines can also consume data.

# In Python 2.5, a slight modification to the yield statement was introduced, now yield can also be used as expression. For example on the right side of the assignment 
# line = (yield)