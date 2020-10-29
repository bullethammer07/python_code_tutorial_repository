#----------------------
# Python f-strings
#----------------------

#-------------------------------------------------------------------------
# The Usual way :
# Printing multiple parameters have to be passed as a tuple
print("\n")
name = "Jayant"
hobby = "coding"
a = "The name is %s and he likes %s" % (name, hobby)
print("Using string formatting : ",a)

#-------------------------------------------------------------------------
# Using .format()
print("\n")

# Way 1
# The elements in format() get assigned to the empty '{}' respectively asper position.
print("Using .format() : ", "My name is {} and I like to {}".format("Jayant", "Code"))

# Way 2
# The elements in format() get assigned as per the 'index' specified in the curly braces {<index>}
print("Using .format() : ", "My name is {1} and I like to {0}".format("Code", "Jayant"))

#-------------------------------------------------------------------------
# Using fstring:
# by starting a string with an 'f' you can print variable by calling the variables inside curly braces, for eg:

print("\n")
print("Using fstrings : ", f"My name is {name} and I like to do {hobby}") # here 'name' and 'hobby' are already declared variables.