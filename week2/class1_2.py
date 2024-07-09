# This file is on python modules
from module import add
from multiply import multiply_numbers
from module import divide

def calculator(operation, value1,  value2=None ):
    # Operation = Add, Subtract, Divide, Multiply

    if operation == "Add":
        return add(value1, value2)
    elif operation == "Subtract":
        return value1 - value2
    elif operation == "Divide":
       return value1/value2
    elif operation == "Multiply":
        return multiply_numbers.multiply_number(value1, value2)
    else:
        return "Unknown Operation"
    


def add(val1, val2):
    return val1 + val2