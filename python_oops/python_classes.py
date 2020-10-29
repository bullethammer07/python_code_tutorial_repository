# One of the popular approaches to solve a programming problem is by creating objects. This is known as Object-Oriented Programming (OOP).

# An object has two characteristics:
#   attributes
#   behavior

# In Python, the concept of OOP follows some basic principles:

#-------------------------------------------------------------------------------------------------------------------------
# Class :
# A class is a blueprint for the object.
# We can think of class as a sketch of a parrot with labels. It contains all the details about the name, colors, size etc.

#-------------------------------------------------------------------------------------------------------------------------
# Object :
# An object (instance) is an instantiation of a class. When class is defined, only the description for the object is defined.
# Therefore, no memory or storage is allocated.
#  eg : obj = some_class()

class some_class:
    # specifying some attributes
    name = "Jayant"
    age = 27
    desig = "Engg"

    # specifying some behavior
    def class_info(self):
        print("This is the class information")

    pass

class_inst = some_class()

# calling some class behavior
class_inst.class_info()

# Adding another attribute to the class, even tho it is not present as part of the class
class_inst.team = "ASIC"
print("My team is : ", class_inst.team)