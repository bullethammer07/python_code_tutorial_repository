# python variable scopes : local and global variables

l = 10  # This is a global variable by the name 'l'
l2 = 20 # # This is another global variable by the name 'l2'

def function1(n):
    l = 5 # This is another variable by the name 'l' but this is local to the function
          # NOTE : however if you comment or remove this variable, the function will print 'l' as 10 (i.e the global value)
          #        this is because the function first looks for the variable in the loval scope, If it fins in the local scope it prints,
          #        otherwise it looks for the variable in the global scope.
          #        If the variable is not found even in the global scope. It will return an error.

    m = 8 # this is also another local variable to the function

    # If we try to alter the value of a global variable (for eg 'l2'), WE WONT BE ABLE TO DO THAT (As we go not have permission to alter a global variable)
    # This will return an  error : UnboundLocalError: local variable 'l2' referenced before assignment
    # l2 = l2 + 1 # UNCOMMENT TO RUN This portion

    # IMPT NOTE : To give permission to local scope to modify any global variable, we can use the 'global' keyword. for eg.
    global l2
    l2 = l2 + 1
    print(l2)

    print(l, m)
    print(n , "Printing done")

function1("My name is slim shady")
print(l) # This will print the global variable 'l' i.e 10 beacuse this print looks for 'll
         # and finds it in the global scope.