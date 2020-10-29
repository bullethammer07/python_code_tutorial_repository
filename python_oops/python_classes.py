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
    # NOTE : 1. All attributes specified inside the class are 'class variables', they are shared by all instances(object) of the class.
    #        2. These attributes cannot be overridden from the object instance.
    name = "Jayant"
    age = 27
    desig = "Engg"

    # specifying some behavior
    def class_info(self):
        print("This is the class information")

    pass

# creating an object of type class
class_inst = some_class()

# calling some class behavior
class_inst.class_info()

# Adding another attribute to the class, even tho it is not present as part of the class
# NOTE : All attributes added from the object are 'instance variables'. They are local copies of the object made and specific to the object made from.
#        They do not alter any of the class attributes.
class_inst.team = "ASIC"
class_inst.proj = "subsystem verif"
print("My team is : ", class_inst.team)
print("Project is : ", class_inst.proj)