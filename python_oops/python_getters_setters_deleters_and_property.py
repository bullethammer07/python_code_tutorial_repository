# Python getters, setters, deleters and property

#------------------------------------
#             PART 1                 
#------------------------------------

# To understand the idea behind getters and setters, we need to understand a few things.

# for eg. Class below takes the first name and last name as initilalization parameters and sets an email accrodingly

class Employee:

    # Class Constructor
    # it takes fname and lname and creates an email id usin the parameters.
    def __init__(self, fname, lname):
        print(f"Creating Employee object for : {fname} {lname}")
        self.fname = fname
        self.lname = lname
        self.email_id = f"{self.fname}.{self.lname}@gmail.com"

    # function to print the employee 'fname' and 'lname'
    def print_emp(self):
        return f"Employee name : {self.fname} {self.lname}"

    # function to print the employee 'email_id'
    def print_email(self):
        return self.email_id

# creating an object of  class 'Employee'
emp1 = Employee("Jayant", "Yadav")

# Now we will try printing the name email id of the created object
print(emp1.print_emp())
print(emp1.print_email())

# Now what will happen if we change the fname of the emp1 object. Will the email id also reflect the made changes.
# for eg changing the name from "Jayant" to "Kapil"
print("\n")
emp1.fname = "Kapil"
print(emp1.print_emp()) # The name will change to Kapil Yadav
print(emp1.print_email()) # However, the mail ID will still be Jayant.Yadav@gmail.com
                          # Since the email_id attribute was set during construction.

#------------------------------------
#             PART 2                 
#------------------------------------

# One way the above problem is solved by returning the email thru a function. 
# for eg. (We will use the same class, just with another name this time : Employee2)

class Employee2:

    # Class Constructor
    # it takes fname and lname and creates an email id usin the parameters.
    def __init__(self, fname, lname):
        print(f"Creating Employee object for : {fname} {lname}")
        self.fname = fname
        self.lname = lname

    # function to print the employee 'fname' and 'lname'
    def print_emp(self):
        return f"Employee name : {self.fname} {self.lname}"

    # function to print the employee 'email_id'
    def print_email(self):
        return f"{self.fname}.{self.lname}@gmail.com"

# Doing the same stuff we dif before
print("-------------------------------------------------")
# creating an object of  class 'Employee2'
emp2 = Employee2("Jayant", "Yadav")
print(emp2.print_emp())
print(emp2.print_email())
emp2.fname = "Kapil"
print(emp2.print_emp()) # The name will change to Kapil Yadav
print(emp2.print_email()) # Now the email_id will be returned properly
print("\n")

# IMPT NOTE :
#  1. The above method however does not follow the real 'Encapsulation' implementation.
#  2. We tried to access email_id as a function instead of an attribute. which isn't a recommended practice.

# NOW WHAT IF WE WANT TO ACCESS 'email_id' as an attribute instead of a function.
# for this we can use the property() function.
# NOTE : refer how property() works in the examples in "/python_concepts_and_basics/python_inbuilt_functions.py" : line : 1142

#------------------------------------
#             PART 3                 
#------------------------------------

# using @property decorator

class Employee3:

    # Class Constructor
    # it takes fname and lname and creates an email id usin the parameters.
    def __init__(self, fname, lname):
        print(f"Creating Employee object for : {fname} {lname}")
        self.fname = fname
        self.lname = lname

    # function to print the employee 'fname' and 'lname'
    def print_emp(self):
        return f"Employee name : {self.fname} {self.lname}"

    # using @property decorator to make a setter
    @property
    def email_id(self):
        return f"{self.fname}.{self.lname}@gmail.com"

# Doing the same stuff we did before
print("-------------------------------------------------")
emp3 = Employee3("Jayant", "Yadav")
print(emp3.print_emp())
print(emp3.email_id)
emp3.fname = "Kapil"
print(emp3.print_emp()) # The name will change to Kapil Yadav
print(emp3.email_id) # Now we are able to use email_id as an attribute by using the @property decorator

# Lets see what happens if we try to set some value to email_id
# emp3.email_id = "ankit.gupta@gmail.com" # UNCOMMENT TO RUN : Thise will return an Exception : AttributeError: can't set attribute
                                          # NOTE : To overcome this problem refer : PART 4
print("\n")

#------------------------------------
#             PART 4                 
#------------------------------------

# Now what if we want to change the 'fname' and 'lname' is the email_id was changed ?
# i.e if the email_id is set to foe eg Ankit.Gupta@gmail.com then  the fname and lname should also change to 'Ankit' and 'Gupta' respectively.
# for such cases we will use setter.

# In such cases you need to create a setter function for which you want to change the values for.
# In this case we need a setter for email_id.

class Employee4:

    # Class Constructor
    # it takes fname and lname and creates an email id usin the parameters.
    def __init__(self, fname, lname):
        print(f"Creating Employee object for : {fname} {lname}")
        self.fname = fname
        self.lname = lname

    # function to print the employee 'fname' and 'lname'
    def print_emp(self):
        return f"Employee name : {self.fname} {self.lname}"

    # using @property decorator to make a setter
    @property
    def email_id(self):
        return f"{self.fname}.{self.lname}@gmail.com"

    # making a setter
    @email_id.setter
    def email_id(self, str):
        print("Setting fname and lname to new values ...")
        part1 = str.split("@")[0]
        self.fname = part1.split(".")[0]
        self.lname = part1.split(".")[1]
        
# Doing the same stuff we did before
print("-------------------------------------------------")
emp4 = Employee4("Jayant", "Yadav")
print(emp4.print_emp())
print(emp4.email_id)
emp4.fname = "Kapil"
print(emp4.print_emp()) # The name will change to Kapil Yadav
print(emp4.email_id)

# Lets see what happens now when we try to set the email_id
emp4.email_id = "ankit.gupta@gmail.com" # now this will run without any error
# Also the above setting of 'email_id' has set the fname and lname of the object, which we can see below
print(emp4.fname, emp4.lname) # this will print ankit gupta
print(emp4.email_id) # this will print ankit.gupta@gmail.com

# NOTE : Now what if we try to delete the 'email_id' attribute
# del emp4.email_id # UNCOMMENT TO RUN : This will return an Exception : AttributeError: can't delete attribute
                    # NOTE : To delete this attribute we must make a 'deleter'
                    #        refer PART 5
print("\n")
           
#------------------------------------
#             PART 5                 
#------------------------------------

class Employee5:

    # Class Constructor
    # it takes fname and lname and creates an email id usin the parameters.
    def __init__(self, fname, lname):
        print(f"Creating Employee object for : {fname} {lname}")
        self.fname = fname
        self.lname = lname

    # function to print the employee 'fname' and 'lname'
    def print_emp(self):
        return f"Employee name : {self.fname} {self.lname}"

    # using @property decorator to make a setter
    @property
    def email_id(self):
        if ((self.fname == None) or (self.lname == None)):
            return f"email not set .... Please set it using Setter !!..."
        return f"{self.fname}.{self.lname}@gmail.com"

    # making a setter
    @email_id.setter
    def email_id(self, str):
        print("Setting fname and lname to new values ...")
        part1 = str.split("@")[0]
        self.fname = part1.split(".")[0]
        self.lname = part1.split(".")[1]
        
    # making a deleter
    @email_id.deleter
    def email_id(self):
        # NOTE : In OOPs it is generally not recommended to delete something.
        #        instead set it to 'None'
        self.fname = None
        self.lname = None
        
# Doing the same stuff we did before
print("-------------------------------------------------")
emp5 = Employee5("Jayant", "Yadav")
print(emp5.print_emp())
print(emp5.email_id)
emp5.fname = "Kapil"
print(emp5.print_emp()) # The name will change to Kapil Yadav
print(emp5.email_id)

# Lets see what happens now when we try to set the email_id
emp5.email_id = "ankit.gupta@gmail.com"
# Also the above setting of 'email_id' has set the fname and lname of the object, which we can see below
print(emp5.fname, emp4.lname) # this will print ankit gupta
print(emp5.email_id) # this will print ankit.gupta@gmail.com

# now trying to delete the 'email_id' attribute
del emp5.email_id # this will now execute
# printing the email id after deleting
print(emp5.email_id)

#------------------------------------
#            OUTPUT                  
#------------------------------------

# Creating Employee object for : Jayant Yadav
# Employee name : Jayant Yadav
# Jayant.Yadav@gmail.com
# 
# 
# Employee name : Kapil Yadav
# Jayant.Yadav@gmail.com
# -------------------------------------------------
# Creating Employee object for : Jayant Yadav
# Employee name : Jayant Yadav
# Jayant.Yadav@gmail.com
# Employee name : Kapil Yadav
# Kapil.Yadav@gmail.com
# 
# 
# -------------------------------------------------
# Creating Employee object for : Jayant Yadav
# Employee name : Jayant Yadav
# Jayant.Yadav@gmail.com
# Employee name : Kapil Yadav
# Kapil.Yadav@gmail.com
# 
# 
# -------------------------------------------------
# Creating Employee object for : Jayant Yadav
# Employee name : Jayant Yadav
# Jayant.Yadav@gmail.com
# Employee name : Kapil Yadav
# Kapil.Yadav@gmail.com
# Setting fname and lname to new values ...
# ankit gupta
# ankit.gupta@gmail.com
# 
# 
# -------------------------------------------------
# Creating Employee object for : Jayant Yadav
# Employee name : Jayant Yadav
# Jayant.Yadav@gmail.com
# Employee name : Kapil Yadav
# Kapil.Yadav@gmail.com
# Setting fname and lname to new values ...
# ankit gupta
# ankit.gupta@gmail.com
# email not set .... Please set it using Setter !!...