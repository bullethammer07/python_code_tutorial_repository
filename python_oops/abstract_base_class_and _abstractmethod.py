# Python Abstract baseclass and @abstractmethod

# There are times when we need to make a class that acts specifically as a base class for others.
# for eg, we make a base class called 'Engine', now we want to enforce and make sure that every class derived from 'Engine'
#         must implement some particular method.
#         For this we must use the @abstractmethod

# NOTE : You also cannot make/create object of the abstract base class.
#        for eg. You cannot create object instance of the 'Engine' class below.

# for making abstract methods and class we need to import 'ABCmeta' and 'abstractmethod' from the 'abc' module

from abc import ABCMeta, abstractmethod

class Engine(metaclass=ABCMeta):

    # MAKING AN ABSTRACT METHOD
    # this method has to be present in every class derived from 'Engine'
    @abstractmethod
    def engine_cc(self):
        return 0

# now making a class 'V_twin' from 'Engine'

class V_twin(Engine):

    num_of_cylinders = 2

    # making an init method
    def __init__(self, num_valve, bore):
        self.num_of_valves = num_valve
        self.bore = bore

    # NOTE : If we do not implement the 'engine_cc' method here in the derived class.
    #        any object made of the 'V_twin' class will return an exception. TypeError: Can't instantiate abstract class V_twin with abstract method engine_cc
    #        we can try that by commenting out the below 'engine_cc' method.
    def engine_cc(self):
        return 600

    # implementing a __repr__ function
    def __repr__(self):
        return f"Num of cylinders : {self.num_of_cylinders} , Num of Valves : {self.num_of_valves}, Bore : {self.bore}"

# Making an object of class 'V_twin'
vt1 = V_twin(8, 12)
print(vt1)

# Trying to create object of the abstract base class 'Engine'
# eng = Engine() # UNCOMMENT TO RUN : This will return an exception : TypeError: Can't instantiate abstract class Engine with abstract method engine_cc