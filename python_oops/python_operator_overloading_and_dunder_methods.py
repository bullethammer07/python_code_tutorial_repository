# Python Operator overloading and Dunder (magic) methods

class Student:
    no_of_lectures = 15

    # Methods that start and end with '__' are called as dunder methods
    # __init__ is also a Dunder method
    def __init__(self, name, cls, section):
        self.name = name
        self.cls = cls
        self.section = section

    def print_stud(self):
        return {f"name : {self.name}  class : {self.cls}  section : {self.section}"}

    @classmethod
    def update_lectures(cls, num_lec):
        cls.no_of_lectures = num_lec

    # Here we have overridden the __add__ operator and given is some new functionality
    # now it will return both the 'name' attribute of each object when '+' is called
    def __add__(self, other):
        return(f"Name : {self.name} and {other.name}")

# now if we make objects of the 'Student' Class
# nothing out of the ordinary here, just two object instances get
std1 = Student("Amit", 10, "C")
std2 = Student("Mohit", 11, "D")

# but if we try doing something vague like : (std1 + std2) , which does not make any sense.
# then it will return with an exception. i.e <TypeError: unsupported operand type(s) for +: 'Student' and 'Student'>
# This is because the addition operator '+' internally calls the __add__ method which does not know what to do when two objects are passed.


# Thus we can override the __add__ operator, and define any desired new functionality to it.
# observe how we have overridden __add__ in the above class
print(std1 + std2)

# NOTE :
# Below is a list of all inbuilr Dunder menthods that can be overridden.
# Refer link (Section : Mapping Operators to Functions) : https://docs.python.org/3.9/library/operator.html