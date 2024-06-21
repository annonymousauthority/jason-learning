# This file is on python modules
from module import add

def calculator(operation, value1,  value2=None ):
    # Operation = Add, Subtract, Divide, Multiply

    if operation == "Add":
        return add(value1, value2)
    elif operation == "Subtract":
        return value1 - value2
    elif operation == "Divide":
       return value1/value2
    elif operation == "Multiply":
        return value1 * value2
    else:
        return "Unknown Operation"
    
