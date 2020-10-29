# self and init in classes

# making a small employee class

class Employee:
    no_of_leaves = 10

    # defining a function to print the content
    def print_data(self):  # NOTE : When we make any function self automatically comes as the argument.
                           #        here self points to the object that will call this function.
                           #        for eg. if below emp2 call the 'print_data' function, then self referes to the object emp2

        print(f"The Data is : {self.__dict__}")

# creating two objects of the employee class
emp1 = Employee()
emp2 = Employee()

# adding instance variables to both the objects
emp1.name = "Jayant"
emp1.team = "ASIC"
emp1.proj = "Subsystem verif"

emp2.name = "Abdul"
emp2.team = "SoC"
emp2.proj = "Low Power"

print(emp1.print_data())
print(emp2.print_data())

#------------------------------------------------------------------------------------------------------------------------------
# In the above method, we have to separately add instance variables to each object after the object is created.
# NOTE : we can avoid this by creating a constructor, which will return an initialized value of the object along with the arguments passed.

# Definition of Constructor : Constructors are special class functions which performs initialization of every object.
#                             The Compiler calls the Constructor whenever an object is created.
#                             Constructors initialize values to object members after storage is allocated to the object.

# constructors in python are made using the __init__ function

# for eg : creating another class
print("\n")
class Employee2:
    num_of_leaves = 20

    # __init__ function encapsulates all the stuff you want to do when the object is created.
    def __init__(self, emp_name, emp_team, emp_proj):
        self.name = emp_name
        self.proj = emp_proj
        self.team = emp_team

    # defining a function to print the content
    def print_data(self):
        print(f"The Data is : {self.__dict__}")

emp_1 = Employee2("Jayant", "ASIC", "debug") # Here 'instance variables' are automatically created by the constructor by passing them as arguments
emp_2 = Employee2("Abdul", "SoC", "analog")

emp_1.print_data()
emp_2.print_data()

# print(Employee2.team) # UNCOMMENT TO RUN : This will return an exception 'AttributeError' as class 'Employee2' does not have class variable
                        # of name 'team'