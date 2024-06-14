scores = [1,2,25,65,75,47]
names = ["Augustine", "Jason", "Mikel", "President"]
myName = "Augustine"
lowercase = "victory"
convertToUppercase = lowercase[0].upper() + lowercase[1:]

fullName = "augustine victor"

print(fullName.split(" ")) # ["augustine", "victor"]

def capitalizeFirstCharacter(char):
    capital = ""
    for value in char:
        if value == char[0]:
            capital += value.upper()
        else:
            capital += value
    return capital

print(convertToUppercase)
print(capitalizeFirstCharacter(lowercase))


# for value in scores:
#     print(value)

# for value in names:
#     print(value)

# for value in myName:
#     print(value) 
