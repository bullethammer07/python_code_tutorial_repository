# Python Multiple Inheritance

# Here we have made an employee class with some attributes and methods

class Employee:

    weekly_mandate_work_hours = 40
    sports_room_open = "YES"
    val = 10 # attribute of same name is present in Biker

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

# Here we are making a separate class in itself called 'Biker'

class Biker:
    val = 20 # attribute of same name is present in Employee

    def __init__(self, biker_name, bike_name, bike_cc):
        self.name = biker_name
        self.bike_name = bike_name
        self.bike_cc = bike_cc

    def print_biker(self):
        print(f"Biker name : {self.name} .... Bike name : {self.bike_name} .... Bike CC : {self.bike_cc}")

# making a few objects of the class and initializing them using the constructor
emp_1 = Employee("Jayant", "ASIC", "subbsystem verif")
emp_2 = Employee("Nikhil", "RF", "Antenna")

# making a object of class Biker
biker_1 = Biker("Arav", "Duke 390", "375")

#----------------------------------------------------------------------------------
# making a class which is inherited from both 'Employee' and 'Biker'

class Biker_Employee(Employee, Biker): # NOTE : Here order of the the classes is very important, becasue the methods and variables of the class that is specified first
                                       #        will take precedence. (Here the variables and methods of Employee will take precedence over Biker as it is specified first)

    # Adding attributes to this class
    num_of_kms_driven = 0
    val = 30

    def kms_driven(self):
        return self.num_of_kms_driven
    pass

# making an object of class 'Biker_Employee'
bike_emp_1 = Biker_Employee("Karan", "ASIC", "UFS")  # NOTE : Here, We will need to specify the constructor arguments as per the requirements of 'Employee'
                                                     # as it will take preference (since specified first),

# bike_emp_1.print_biker(); # UNCOMMENT TO RUN : This will return an Exception as the attributes related to 'Biker' portion are not initialized.

# Some points related to multiple inheritance :
#  1. In the multiple inheritance scenario, any specified attribute is searched first in the current class.
#     If not found, the search continues into parent classes in depth-first, left-right fashion without searching the same class twice.
#  2. So, in the above example of 'Biker_Employee' class the search order is [Biker_Employee -> Employee/Biker]. This order is also called linearization of MultiDerived class
#     and the set of rules used to find this order is called Method Resolution Order (MRO).
#  3. MRO must prevent local precedence ordering and also provide monotonicity. It ensures that a class always appears before its parents.
#     In case of multiple parents, the order is the same as tuples of base classes.
#  4. MRO of a class can be viewed as the __mro__ attribute or the mro() method. The former returns a tuple while the latter returns a list.

print("\n")
print(bike_emp_1.kms_driven())
print(f"Printing a common attribute : {bike_emp_1.val}") # printing a common attribute between 'Employee' and 'Biker' : val
                                                         # here if val is not present in 'Biker_Employee' the attribute of the first class passed will take precedence.
                                                         # in this case val is present in 'Biker_Employee' ... but if commented , val of 'Employee' will come into picture.

print(Biker_Employee.__mro__) # This returns a tuple
print(Biker_Employee.mro()) # this returns a list