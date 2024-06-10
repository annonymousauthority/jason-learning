## int, str, bool, float

## list, tuple, set, dict

## bytes, bytearray

def contatenate_example(a,b):
    return a + b

print(contatenate_example("12","5"))

def parse_value(value):
    # Parse Number to string
    return int(value)

print(parse_value("12"))


def add_numbers(a, b):
    result = []
    for num in a:
        sum = num + b
        result.append(sum)
    return result


print(add_numbers([1,2,4,5], 5)) # [6,7,9,10]

def combine_values_in_list(list):
    value_tracker = ""
    for value in list:
        if(isinstance(value, str)):
            value_tracker += value
        else:
            value_tracker += str(value)
    
    return value_tracker


list1 = ["Augustine", "Jason", "Mummy"] # AugustineJasonMummy
list2 = [21, 12, 300] # 333
list3 = ["Augustine", 33, "Jason", "Mummy", 333] #Augustine33JasonMummy333

print(combine_values_in_list(list3))