#-----------------------------
#  Python Function Caching    
#-----------------------------

# Some understanding :
# consider a function f(x), that takes quite some time to return an output for parameter 'x'
# Now in a scenario where f(x) is called multiple times for parameter 'x' it usually would not make sense to spend the same long time to compute the return value.
# In such scenarios we can cache a particular function
# so if f(x) is cached for parameter 'x', the next time f(x) is called with parameter 'x' the output will be spontaneous.

# In Python we have to import 'lru_cache' decorator from 'fuctools' inbuilt module to cache a particular function

#-----------------------------------------------------------------------------------------------------------------
# Example 1 :
# Consider a function that takes some time to return a value.
# Here we will mddel that using sleep

import time

def return_sum(a, b):
    time.sleep(3) # sleep for 3 seconds
    return a + b

print(return_sum(2, 3)) # Here 5 will be printed only after 3 seconds

# Now assume we have multiple instances of the above function : like :

# print(return_sum(2, 3))
# print(return_sum(2, 3))
# print(return_sum(2, 3))

# Now each function will take 3 secs each to compute.
# However if we are able to cache the output of the function for that parameter, we can avoid long runs

# for this we use the "lru_cache" from "functools"

from functools import lru_cache

@lru_cache(maxsize=2) # only the outcome of the last 2 calls will be cached
def return_sum2(a, b):
    time.sleep(3) # sleep for 3 seconds
    return a + b

# since maxsize was selected as 2, only the last two call with parameters (2,2) and (2,3) will be cached.
print(return_sum2(1, 3))
print(return_sum2(2, 2))
print(return_sum2(2, 3))

# Now if we call the function with parameters (2, 3) it will be executed quickly without consuming time
# since the function with this parameter was cached in the last two calls. (as defined by maxsize)
print(return_sum2(2, 3))