# Class Method

class Employee:

    weekly_mandate_work_hours = 40
    sports_room_open = "YES"

    def __init__(self, emp_name, emp_team, emp_proj):
        self.name = emp_name
        self.team = emp_team
        self.proj = emp_proj

    # A class method is a method which is bound to the class and not the object of the class.
    # A class method receives the class as implicit first argument, just like an instance method receives the instance.
    # They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
    # It can modify a class state that would apply across all the instances of the class.
    #   For example, it can modify a class variable that would be applicable to all the instances.
    @classmethod
    def change_work_hours(cls, new_hours): # here 'cls' will refer to the class of which the instance is used to call
                                           # for eg. if we call emp_2.change_work_hours(<new value>) , it will pick the class of emp_2 i.e 'Employee' as 'cls'
                                           # using this reference we can modify the 'class variables'
        cls.weekly_mandate_work_hours = new_hours

    # A static method does not receive an implicit first argument.
    # A static method is also a method which is bound to the class and not the object of the class.
    # A static method can’t access or modify class state.
    # It is present in a class because it makes sense for the method to be present in class.
    @staticmethod
    def simple_adder(arg1, arg2):
        print(f"Sum of two numbers :: {arg1 + arg2}")


emp_1 = Employee("Jayant", "ASIC", "subbsystem verif")
emp_2 = Employee("Nikhil", "RF", "Antenna")

# NOTE : We have seen before that we cannot override the 'class variable' from the object/instances.
#        trying to do so creates a separate 'instance variable' for the instance no no changes to the 'class variable' happens
#        Thus to modify the 'class variable' (weekly_mandate_work_hours) we will need to modify from the class itself.
#        i.e : Employee.weekly_mandate_work_hours = <new value>
#              This will make the value common for all objects of the class who are sharing that variable.

# Now if we try to modify the 'weekly_mandate_work_hours' using the object 'emp_1' by calling the function 'change_work_hours',
# it will modify the values for 'emp_2' as well

print("\n")
print("Work hours per week for emp_1 : ", emp_1.weekly_mandate_work_hours)
print("Work hours per week for emp_2 : ", emp_2.weekly_mandate_work_hours)

emp_1.change_work_hours(50)
print("Work hours per week for emp_1 : ", emp_1.weekly_mandate_work_hours)
print("Work hours per week for emp_2 : ", emp_2.weekly_mandate_work_hours)

emp_1.simple_adder(5, 7)