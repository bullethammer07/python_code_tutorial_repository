var1 = "Hello world"
var2 = 4
var3 = 3.14

print(type(var1))
print(type(var2))
print(type(var3))

# Storing a variable of type: 'type'
value = type(var1)
print(type(value))

#-----------------------------------------
# Casting variable values

# Below both values are of type string
str_var1 = "52"
str_var2 = "35"

int_cast_var1 = int(str_var1)  # Casting string value str_var1 to int
int_cast_var2 = int(str_var2)  # Casting string value str_var2 to int

print(type(int_cast_var1),type(int_cast_var2),int_cast_var1+int_cast_var2)

"""
--------------------------------------------------------------------------
 Taking an Input value and casting is accordingly
 There are two ways of taking input :

1. Either print and then store in a variable. for eg.

print("Enter Number :");
val1 = input()                 <- This stores the value taken from the console in 'val1' in string format

2. Put the print statement in the input command itself. for eg.

val1 = input("Enter Number :")
------------------------------------------------------------------------- 
"""

print("Enter number A : ")
val1 = input()

val2 = input("Enter number B : ")

print(type(val1),type(val2))
print(int(val1) + int(val2))




