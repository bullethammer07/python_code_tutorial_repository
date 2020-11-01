# Python __repr__ and __str__ dunder methods

class Student:
    no_of_lectures = 15

    def __init__(self, name, cls, section):
        self.name = name
        self.cls = cls
        self.section = section

    def print_stud(self):
        return {f"name : {self.name}  class : {self.cls}  section : {self.section}"}

    @classmethod
    def update_lectures(cls, num_lec):
        cls.no_of_lectures = num_lec

    def __add__(self, other):
        return(f"Name : {self.name} and {other.name}")

    # making the __repr__ dunder method
    def __repr__(self):
        return f"Student ('{self.name}', {self.cls}, '{self.section}')"

# now if we make objects of the 'Student' Class
# nothing out of the ordinary here, just two object instances get
std1 = Student("Amit", 10, "C")

# NOTE : Here we directly printer std1, without calling __repr__(), but still __repr__() method got picked
#        You can use this a a method to print classes.
#        Without the __repr__(), if we printedt he object, it will return something unpresentable like :
#        <__main__.Student object at 0x000001B64817EFA0>

print(std1)

#----------------------------------------------------------------------------------------------------------
# Implementing both __repr__ and __str__
# NOTE : When both __repr__ and __str__ are implemented:
#   1. If you print an object like : print(<object>), the __str__ method will take precedance over the __repr__
#   2. If you call repr() explicitly, repr() will be picked.
#   3. If you cann the str() method but there is not definition -f __str__ in the class, then __repr__ will be picker.

class Student2:
    no_of_lectures = 15

    def __init__(self, name, cls, section):
        self.name = name
        self.cls = cls
        self.section = section

    def print_stud(self):
        return {f"name : {self.name}  class : {self.cls}  section : {self.section}"}

    @classmethod
    def update_lectures(cls, num_lec):
        cls.no_of_lectures = num_lec

    def __add__(self, other):
        return(f"Name : {self.name} and {other.name}")

    # making the __repr__ dunder method
    def __repr__(self):
        return f"Student ('{self.name}', {self.cls}, '{self.section}')"

    def __str__(self):
        return f"Student (The student name is : '{self.name}', Class : {self.cls}, Section : '{self.section}')"

sinst = Student2("Mohit", 11, "D")

# Since the above class has both __repr__ and __str__, __str__ will take precedence over __repr__ when the object is printer.
print(sinst)
# calling explicitly using repr
print(repr(sinst))

# run below code after commenting the __str__ method in the class above. This will call the __repr__ even tho we have called it using str()
print(str(sinst))