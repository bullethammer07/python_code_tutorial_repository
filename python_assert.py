# assert / assertions in python

# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# What is Assertion ?.

# Assertions are statements that assert or state a fact confidently in your program.
# For example, while writing a division function, you're confident the divisor shouldn't be zero, you assert divisor is not equal to zero.

# Assertions are simply boolean expressions that check if the conditions return true or not.
# If it is true, the program does nothing and move to the next line of code. However, if it's false, the program stops and throws an error.

# It is also a debugging tool as it brings the program on halt as soon as any error is occurred and shows on which point of the program error has occurred.



# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# Python 'assert' Statement
# Python has built-in 'assert' statement to use assertion condition in the program.
# assert statement has a condition or expression which is supposed to be always true.
# If the condition is false assert halts the program and gives an AssertionError.

# Syntax : assert <condition>
#          assert <condition>,<error message>
#            In Python we can use assert statement in two ways as mentioned above.
#              1. assert statement has a condition and if the condition is not satisfied the program will stop and give AssertionError.
#              2. assert statement can also have a condition and a optional error message.
#                 If the condition is not satisfied assert stops the program and gives AssertionError along with the error message.

# Eg. Using assert in a function incase an unsupported argument is passed

def function1(val):
    """
      Calculates the sum or the difference based on the argument passed.
      If argument passed is anything other than 0 or 1, an assertion is fired.
    """
    assert ((val == 1) or (val == 0)), "Unsupported arguments" # Using Assertion with an ErroR Message

for val in [0, 1, 2]: # Here AssertionError will come when argument as 2 will be made for function call for function1()
    print("Executing function for val : ", val)
    function1(val)