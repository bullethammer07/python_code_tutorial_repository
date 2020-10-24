
def function1():
    x = 20
    f1_local = 30

    def function2(): # This is a nested function

        global x
        x = 88

    print("Before calling function2() : ", x) # This will print x as 20
    function2()
    print("After calling function2() : ", x) # This will still print x as 20, because 'gobal x' inside function 2 does not go one step up to function1 to resolve value of x
                                             # instead it will jump directly to the top global scope (outside function1).
                                             # if it finds x it will take that value for modification.
                                             # However since here there is no x in top global scope, the 'global x' in function 2 will create a global variable x in top scope
                                             # whose value is now modified to 88

function1()
print(x) # This will print 88 , as this is the global variable 'x' created at the topmost scope when function2() was called.