
def addNumbers(num1, num2):
    # num1 + num2
    result = num1 + num2
    return result

def shortAddition(num1, num2):
    return num1 + num2

# string1 = "Cal" string2 = "Mata"
#return string1 = "Mal" && string2 = "Cata"

def swapIndexValue(string1, string2):
    # Extract first value for each string, val1 = C, val2 = M
    # Extract the remaining values for each string. remainVal1 = al, remainVal2 = ata
    # Merge the first value with the opposing string values, --> String1 = M+al, String2 = C+ata

    # Step 1
    val1 = string1[0]
    val2 = string2[0]

    # Step 2
    remainVal1 = string1[1:]
    remainVal2 = string2[1:]

    # Step 3
    merge1 = val1 + remainVal2
    merge2 = val2 + remainVal1

    print(merge2, merge1)


swapIndexValue("Cal", "Mata")

import USERS


def getUsers(url):
    print(url.USERS[1]["names"])

getUsers(USERS)