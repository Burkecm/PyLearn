# Generate a PW based on user input
import random as rand
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]


print("Welcome to the password generator")

numLetters = int(input("How many letters would you like to use?"))
numSymbols = int(input("how many special characters?"))
numNumbers = int(input("how many Numbers?"))

# Easy Version
# password = ""
# for l in range(0, numLetters):
#     password += rand.choice(letters)

# for s in range(0, numSymbols):
#     password += rand.choice(symbols)

# for s in range(0, numNumbers):
#     password += rand.choice(numbers)

# print(str(password))

# Hard version
password = []
for l in range(0, numLetters):
    password.append(rand.choice(letters))

for s in range(0, numSymbols):
    password.append(rand.choice(symbols))

for s in range(0, numNumbers):
    password.append(rand.choice(numbers))

rand.shuffle(password)
print("".join(password))