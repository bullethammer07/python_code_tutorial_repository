#--------------------------------------------------------------
#             Python lists inbuilt functions
#--------------------------------------------------------------
# abs()              : Returns the absolute value of a secified number.
# all()              : Returns true if all items in an iterable are true, otherwise it returns False.
# any()              : Returns True if any item in an iterable are true, otherwise it returns False.
# ascii()            : Returns a readable version of any object (Strings, Tuples, Lists, etc). function will replace any non-ascii characters with escape characters.
#                      syntax: ascii(object)
# bin()              : Returns the binary version of a specified integer.
# bool()             : Returns the boolean value of a specified object (Any object, like String, List, Number etc).
# bytearray()        : Both bytearray() and bytes() returns a bytearray object.
# bytes()            : Both bytearray() and bytes() returns a bytearray object.

#----------------------------------------------------------------------------------------------------------------------
# abs()
# Description : returns the absolute value of a specified number
# Syntax : abs(n)
#          n : (Required). a number

print("\n")
x = abs(-7.21)
print("abs : ",x) # returns 7.21
y = abs(3+5j)
print("abs : ",y)

#----------------------------------------------------------------------------------------------------------------------
# all() and any()
# Description : all() : returns true if all items in an iterable are true, otherwise it returns false.
#               NOTE : if the iterable object is empty, all() function also returns true.
#               any() : returns True if any item in an iterable are true, otherwise it returns False.
#               NOTE : If the iterable object is empty, the any() function will return False.
# Syntax : all(iterable)
#          iterable : list, tuple, dictioary

print("\n")
list1 = ["Hi","my","name","is","Jayant"]
list2 = ["","","","",""]
list3 = ["Hi","my","name","",""]
list4 = [] # Empty list
print("all : ",all(list1)) # -> returns TRUE
print("all : ",all(list2)) # -> returns FALSE
print("all : ",all(list3)) # -> returns FALSE
print("all : ",all(list4)) # -> returns TRUE

print("any : ",any(list1)) # -> returns TRUE
print("any : ",any(list2)) # -> returns FALSE
print("any : ",any(list3)) # -> returns TRUE
print("any : ",any(list4)) # -> returns FALSE

#----------------------------------------------------------------------------------------------------------------------
# bin()
# Description : Returns the binary version of a specified integer.
#               The result will always start with the prefix 0b.
# Syntax : bin(n)
#          n : (Required). An Integer

print("\n")
print("bin : ",bin(69))

#----------------------------------------------------------------------------------------------------------------------
# bool()
# Description :  returns the boolean value of a specified object.
#                The object will always return True, unless:
#                The object is empty, like [], (), {}
#                The object is False
#                The object is 0
#                The object is N

empty_list = []
empty_tuple = ()
empty_array = {}
print("bool : ",bool(empty_list),bool(empty_tuple),bool(empty_array),bool("xyz"),bool(""))

#----------------------------------------------------------------------------------------------------------------------
# bytearray() and bytes()
# Descriptiom : both bytearray() and bytes() returns a bytearray object.
#               The difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified, and bytearray() returns an object that can be modified.
# Syntax : bytearray(x,encoding,error)
#          bytes(x,encoding,error)
#          x : A source to use when creating a bytearray object.
#               NOTE : If it is an integer, An empty bytearray object of the specified size will be created.
#                    : If it is a string make sure you specify the encoding of the source.
#          encoding : The encoding of the string
#          error : specifies what to do if the encoding fails

print("\n")
print("bytearray : ",bytearray(10)) # -> Output is an empty bytearray of length 10 : bytearray :  bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
print("bytearray : ",bytearray("xyz","big5")) # specify the encoding in double quotes eg. "ascii" or "utf8" etc.

print("\n")
print("bytes : ",bytes(6))
print("bytes : ",bytes("xyz","big5"))