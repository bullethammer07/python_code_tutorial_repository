# Python classmethod as constructor

# Here we are trying too get a constructor behavior, without using the class but instead a behavior of the class.

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
    def alt_const(cls, str): # Defining the alternate constructor, the method takes a string as input.
                             # NOTE : we will be specifying all the attributes of the object to be created via this string.
                             #        for eg, we can pass the name,team & proj in a single string separated by a separator like -> "Jayant/ASIC/subsystems" (Here '/' is the separator)
        obj_vals = str.split("/")

        # now we have all three values of the object to be constructed stored in the list 'obj_vals'
        # we can now return an object 'cls' of the specified values.
        return cls(obj_vals[0], obj_vals[1], obj_vals[2])

        # NOTE : The above two lines can also be condensed into a single line and can  be used in similar way :
        # return cls(*str.split("/") # UNCOMMNET THIS AND COMMENT ABOVE TWO LINES TO RUN


emp_1 = Employee("Jayant", "ASIC", "subbsystem verif")
emp_2 = Employee("Nikhil", "RF", "Antenna")

# Creating emp_3 using alternative constructor method created
emp_3 = Employee.alt_const("Mohit/ML/Vision")

# Printing contents on emp_3
print("emp_3 details : ", emp_3.__dict__)