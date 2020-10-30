#==============================================
#             PUBLIC ATTRUBUTES
#==============================================
# Public Attributes and methods of a class are :
#   1. Visible to own class.
#   2. Visible to Derived Classes.
#   3. Visible to Outside Classes.

# NOTE : All attributes and nethods are by default Public.
#        THIS IS PRETTY STRAIGHT FORWARD TO UNDERSTAND SO MUCH EXAMPLES ARE NOT NECESSARY


#==============================================
#      PROTECTED AND PRIVATE ATTRUBUTES
#==============================================
# Public Attributes and methods of a class are :
#   1. Visible to own class.
#   2. Visible to Derived Classes.
#   3. Not-Visible to Outside Classes.

# NOTE : Protested attribute and method names start with an '_' i.e underscore

# Making a parent class
class Parent:
    var1 = 5  # public variable
    _var2 = 6 # protected variable
    _var3 = 15 # another protectd variable
    __var4 = "private val"

    def print_vars(self):
        print(f"Inside Parent class : {self.var1}")
        print(f"Inside Parent class : {self._var2}")

    @staticmethod
    def _protected_func():
        print("This is protected function of 'Parent' class")

    @classmethod
    def print_pvt_var(cls):
        print("Parent private variable __var4 : ", cls._Parent__var4)

# making a child class derived from parent
class Child(Parent):
    var1 = 55
    _var2 = 10

    def print_parent_private_var(self):
        print(f"parent private val : {self._Parent__var4}")

# making a family class that contains (not derived from) both 'Parent' and 'Child'
class Family:
    p1 = Parent() # instance of Parent inside society
    c1 = Child() # instance of Child Inside family

    # function to try to access public attribute of 'Parent'
    def print_parent_public_attr(self):
        print("Parent public attribute 'var1' : ", self.p1.var1)

    def print_child_public_attr(self):
        print("Child public attribute 'var1' : ", self.c1.var1)

    def print_parent_prot_attr(self):
        print("Parent protected attribute '_var2' : ", self.p1._var2)

    @classmethod
    def temp(cls, p1):
        print(p1._var2)

# making instance of parent
parent_inst1 = Parent()
parent_inst1.print_vars()

# making instance of child
child_inst1 = Child()
child_inst1.print_vars()

# print("printing parent private member : ", child_inst1.__var4)
# printing protected member of Parent from child instance
print(f"Printing paraent protected attribute : {child_inst1._var3}") # This will return 15 as _var3 is protected attribute of base class 'Parent'

# calling a protected function of Parent class from child instance
child_inst1._protected_func() # This will also execute without any issue

print("\n")

# making instance of family
fam_inst1 = Family()
# calling 'print_parent_public_attr' function of fam_inst1
fam_inst1.print_parent_public_attr()
# calling 'print_child_public_attr' function of fam_inst1
fam_inst1.print_child_public_attr()

# trying to print protected attribute of 'Parent' i.e _var from instance of 'Family' using function 'print_parent_prot_attr'
print(fam_inst1.p1._var2)

print("-"*40)
print(parent_inst1.var1)
print(parent_inst1._var2)
print(parent_inst1._var3)
print(parent_inst1._Parent__var4)
print("-"*40)
# print(child_inst1.var1)
# print(child_inst1._var2)
# print(child_inst1.__var4)

print(var1)

