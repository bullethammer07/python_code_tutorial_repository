# Super and method overriding in python

class Parent:
    var1 = 5
    var2 = 6

    def __init__(self):
        self.var3 = 45;
        self.var4 = 55;

class Child(Parent):
    var1 = 10
    var2 = 20

    # overriding __init__ function
    def __init__(self):
        super().__init__()
        self.var3 = 65;
        self.var4 = 75;

par = Parent()
chi = Child()

print(par.var1, par.var2, par.var3, par.var4)
print(chi.var1, chi.var2, chi.var3, chi.var4)