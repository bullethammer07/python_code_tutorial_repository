#--------------------------------------------------------------
#             Python lists inbuilt functions
#--------------------------------------------------------------
# abs()              : Returns the absolute value of a secified number.
# all()              : Returns true if all items in an iterable are true, otherwise it returns false.

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
# all()
# Description : returns true if all items in an iterable are true, otherwise it returns false.
#               NOTE : if the iterable object is empty, all() function also returns true.
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
