#---------------------------------------
#          Python Co-Routines           
#---------------------------------------

# NOTE : An understanding of Python Generators is recommended before understanding coroutines. 

# We all are familiar with function which is also known as a subroutine, procedure, subprocess etc. 
# Subroutines in Python are called by main function which is responsible for coordination the use of these subroutines. 
# NOTE : Subroutines have single entry point. 

#--------------
# Coroutines :
#--------------
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

#--------------------
# Python Coroutine :
#--------------------
# In Python, coroutines are similar to generators but with few extra methods and slight change in how we use yield statement. 
# Generators produce data for iteration while coroutines can also consume data. 

# In Python 2.5, a slight modification to the yield statement was introduced, now yield can also be used as expression. For example on the right side of the assignment 
# line = (yield) 

# NOTE : Whatever value we send to coroutine is captured and returned by (yield) expression. 
#        A value can be send to the coroutine by send() method. 

# Execution of coroutine is similar to the generator. 
# When we call coroutine nothing happens, it runs only in response to the next() and send() method. 
# This can be seen clearly in below example, as only after calling __next__() method, out coroutine starts executing.
# After this call, execution advances to the first yield expression, now execution pauses and wait for value to be sent to 'inst' object.
# When first value is sent to it, it checks for 'val' and print the 'val'.
# After printing 'val' it goes through loop until it encounters name = (yield) expression again.

# Example 1 :
def print_value(val):
    print(f" The value is : {val}")
    
    while True:
        name = (yield)
        print(f"Yield name specified : {name}")

# creating instance of the coroutine and
# calling the coroutine, NOTHING WILL HAPPEN.
inst = print_value(20)

# This will start execution of coroutine and  
# Prints first line.
# and advance execution to the first yield expression 
inst.__next__()

# Sending Inputs
inst.send("Input 1")
inst.send("Input 2")
inst.send("Input 3")

#--------------------------
#   Closing a Coroutine
#--------------------------
# Coroutine might run indefinitely, to close coroutine close() method is used.
# When coroutine is closed it generates GeneratorExit exception which can be catched in usual way.
# After closing coroutine, if we try to send values, it will raise StopIteration exception.

inst.send("Input 4")
inst.send("Input 5")
inst.send("Input 6")
inst.close()