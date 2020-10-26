# Python time module

import time

# Refer time documentation at : https://docs.python.org/3/library/time.html
# for description into the time module and functions

# some important and basic functions to know :
#  gmtime()
#  localtime()
#  sleep()

for i in range(50):
    print(time.gmtime())
    print(time.localtime())
    print("\n")
    # trying to typecast
    tpl = tuple(time.gmtime())
    tpl2 = tuple(time.localtime())
    print("Converted Tuple : ", tpl, type(tpl))
    print("Converted Tuple : ", tpl2, type(tpl2))