# Python Single Inheritance

# Here we have made an employee class with some attributes and methods

class Employee:

    weekly_mandate_work_hours = 40
    sports_room_open = "YES"

    def __init__(self, emp_name, emp_team, emp_proj):
        self.name = emp_name
        self.team = emp_team
        self.proj = emp_proj

    @classmethod
    def change_work_hours(cls, new_hours):
        cls.weekly_mandate_work_hours = new_hours

    @staticmethod
    def simple_adder(arg1, arg2):
        print(f"Sum of two numbers :: {arg1 + arg2}")

    @classmethod
    def alt_const(cls, str):
        obj_vals = str.split("/")
        return cls(obj_vals[0], obj_vals[1], obj_vals[2])

# making a few objects of the class and initializing them using the constructor
emp_1 = Employee("Jayant", "ASIC", "subbsystem verif")
emp_2 = Employee("Nikhil", "RF", "Antenna")
# Creating emp_3 using alternative constructor method created
emp_3 = Employee.alt_const("Mohit/ML/Vision")
# Printing contents on emp_3
print("emp_3 details : ", emp_3.__dict__)

# Making another class 'Coder' by extending the class 'Employee'

class Coder(Employee):
    # Here the coder class will have a few additional attributes apart from the base class, for eg experience and previous company.
    # for this we can define the __init__ method for this class separately, as done below.
    def __init__(self, emp_name, emp_team, emp_proj, emp_exp, emp_prev_comp):
        # for now we will use the template used in the base class,
        # however this isnt encouraged , as we must use super() in such scenarios.
        self.name = emp_name
        self.team = emp_team
        self.proj = emp_proj
        self.exp = emp_exp
        self.prev_comp = emp_prev_comp

# Making an object of class 'Coder' using the new constructor made
emp_4 = Coder("Abdul", "Emulation", "Firmware", 4, "Micron")
print("emp_4 details : ", emp_4.__dict__)

# NOTE : Notice that __init__() method was defined in both classes, 'Employee' as well 'Coder'.
#        When this happens, the method in the derived class overrides that in the base class. This is to say,
#        __init__() in 'Coder' gets preference over the __init__ in 'Employee'.

# Generally when overriding a base method, we tend to extend the definition rather than simply replace it.
# (We did not do that here however.. But Still ... It wont block or fail the code, but is not good practice).
# A better option would be to use the built-in function super(). So, super().__init__(<arguments>) is equivalent to Employee.__init__(<arguments>) and is preferred.

#----------------------------------------------------------------------------------------------------------------
# Two built-in functions isinstance() and issubclass() are used to check inheritances.
#   1. The function isinstance() returns True if the object is an instance of the class or other classes derived from it.
#      Each and every class in Python inherits from the base class object.
#   2. Similarly, issubclass() is used to check for class inheritance.

# creating a random class that has no relation with 'Employee' or 'Coder'

class RandomClass:
    pass

print("\n")

print(isinstance(emp_4, Employee)) # True
print(issubclass(Coder, Employee)) # True
print(isinstance(emp_4, RandomClass)) # False