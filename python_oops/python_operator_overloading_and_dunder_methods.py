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

# now if we make objects of the 'Student' Class
# nothing out of the ordinary here, just two object instances get
std1 = Student("Amit", 10, "C")
std1 = Student("Mohit", 11, "D")