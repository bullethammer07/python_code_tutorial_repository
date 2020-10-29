# Difference between Class Variables and Inst variables :

# making a base class of an employee
class employee:
    num_of_leaves = 10  # This is a class attribute or (class variable)
                        # all objects of this class will share this variable.
                        # this cannot be altered from the object


emp1 = employee()  # making an object of type employee
emp2 = employee()

# we can print all the attributes of a class using the __dict__ method

print("Contents of emp1 : ", emp1.__dict__)  # This will come as empty as we have not added anything
print("Contents of emp2 : ", emp2.__dict__)

# Adding local attributes to individual objects
# NOTE : These attributes are local to each of the individual object. They are not added to the class.
emp1.name = "Jayant"
emp1.age = 27
emp1.team = "ASIC"

emp2.name = "Abdul"
emp2.age = 28
emp2.team = "SoC"

# Now printing the contents :
print("Contents of emp1 : ", emp1.__dict__)
print("Contents of emp2 : ", emp2.__dict__)
print("Contents of employee class : ", employee.__dict__) # This will only contain number of leaves and other inbuilt base functions and attributes

# Printing the num of leaves for both employees
print(f"num of leaves of emp1 is : {emp1.num_of_leaves}")  # This will return 10
print(f"num of leaves of emp2 is : {emp2.num_of_leaves}")  # This will also return 10

# If you try to modify the class variable 'num_of_leaves' from the object. A local copy of that variable is made for that object.
# This does not affect the class variable content. for eg.

emp2.num_of_leaves = 20
print(f"After emp2 object modify :: num of leaves of emp2 is : {emp2.num_of_leaves}")
print(f"Contents of 'num_of_leaves' in base class", employee.num_of_leaves) # this will be originally retained

# Only the class can modify its class variables. for  eg.
employee.num_of_leaves = 15
print(f"num of leaves of emp1 is : {emp1.num_of_leaves}")  # Since we did not make any 'instance variable' of 'num_of_leaves' for emp1
                                                           # it will still hold the shared value as present in the 'employee' class
                                                           # This will return 15, since it was chnaged to 15 from the class itself.
print(f"Contents of 'num_of_leaves' in base class", employee.num_of_leaves)  # This will print the current modified value i.e 15.

print("\n")

# Modifying 'num_of_leaves' value in emp1 also :
emp1.num_of_leaves = 25  # Now this will create a separate local variable for instance 'emp1'
print(f"num of leaves of emp1 is : {emp1.num_of_leaves}")  # will return 25
print(f"num of leaves of emp2 is : {emp2.num_of_leaves}")  # will return 20
print(f"Contents of 'num_of_leaves' in base class", employee.num_of_leaves) # will return 15