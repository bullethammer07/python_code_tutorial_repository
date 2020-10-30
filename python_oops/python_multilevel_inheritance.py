# Python Multilevel inheritance

import math

# class for a basic calculator
# returns basic mathematical functions only : +,-,*,/
class Basic_calculator:
    resolution = "16x2"

    @staticmethod
    def return_add(arg1, arg2):
        return (arg1 + arg2)

    @staticmethod
    def return_diff(arg1, arg2):
        return (arg1 - arg2)

    @staticmethod
    def return_prod(arg1, arg2):
        return (arg1 * arg2)

    @staticmethod
    def return_quotioent(arg1, arg2):
        return (arg1 / arg2)

basic_calc_inst = Basic_calculator()
print(f"Basic Calculator : {basic_calc_inst.return_add(1, 2)}")
print(f"Basic Calculator : {basic_calc_inst.return_diff(4, 2)}")
print(f"Basic Calculator : {basic_calc_inst.return_prod(5, 3)}")
print(f"Basic Calculator : {basic_calc_inst.return_quotioent(10, 2)}")

# making an advanced calculator from basic calculator with added functions
class Advanced_calculator(Basic_calculator):
    resolution = "16x4"

    @staticmethod
    def return_factorial(arg1):
        return (math.factorial(arg1))

    @staticmethod
    def return_exp(arg1, arg2):
        return (arg1 ** arg2)

print("\n")

adv_calc_inst = Advanced_calculator()
print(f"Advanced Calculator : {adv_calc_inst.return_add(1, 2)}")
print(f"Advanced Calculator : {adv_calc_inst.return_diff(4, 2)}")
print(f"Advanced Calculator : {adv_calc_inst.return_prod(5, 3)}")
print(f"Advanced Calculator : {adv_calc_inst.return_quotioent(10, 2)}")
print(f"Advanced Calculator : {adv_calc_inst.return_factorial(5)}")
print(f"Advanced Calculator : {adv_calc_inst.return_exp(7, 3)}")

# making scientific calculator from advanced calculator