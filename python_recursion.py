# python recursion

#-----------------------------------
# factorial example using recursion
#-----------------------------------

# n * (n-1) * (n-2) * (n-3) * ..... * 1

def factorial(n):
    fact = n
    if (n == 1):
        fact = 1
    else:
        fact = fact * factorial((n-1)) # calling the same function inside function
    return fact

for val in range(1, 11):
    print(factorial(val))