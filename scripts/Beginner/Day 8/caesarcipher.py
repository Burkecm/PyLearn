alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphaUpper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X""," "Y", "Z"]
# def encrypt(message, shift):
#     encodedMessage = ''
#     for letter in message:
#         if letter.islower():
#             index = alpha.index(letter)
#             indexShifted = (index+shift) % len(alpha)
#             encodedMessage += alpha[indexShifted]
#         else:
#             index = alphaUpper.index(letter)
#             indexShifted = (index+shift) % len(alphaUpper)
#             encodedMessage += alphaUpper[indexShifted]
#     print(encodedMessage)


# def decrypt(messageEncrypted, shift):
#     decodedMessage = ''
#     for letter in messageEncrypted:
#         if letter.islower():
#             index = alpha.index(letter)
#             indexShifted = (index-shift) % len(alpha)
#             decodedMessage += alpha[indexShifted]
#         else: 
#             index = alphaUpper.index(letter)
#             indexShifted = (index-shift) % len(alphaUpper)
#             decodedMessage += alphaUpper[indexShifted]
#     print(decodedMessage)

# choice = input("Type 'encode' to encrypt, type 'decode' to decrypt ")
# validOptions = ["encode", "decode"]
# if choice not in validOptions:
#     print(f"{choice} is not a valid Choice.")
# else:
#     shift = int(input("What is the value of shift? Please enter an integer "))
#     if choice == "encode":
#         message = input("What message would you like to send? ")
#         encrypt(message, shift)
#     else:
#         message = input("What message would you like to receive? ")
#         decrypt(message, shift)


def caesar(direction, message, shift):
    outputMessage = ''
    if direction == "decode":
        shift *= -1
    for letter in message:
        if letter.islower():
            if letter not in alpha:
                outputMessage += letter
            else:
                index = alpha.index(letter)
                indexShifted = (index+shift) % len(alpha)
                outputMessage += alpha[indexShifted]
        else:
            if letter not in alpha:
                outputMessage += letter
            else:
                index = alphaUpper.index(letter)
                indexShifted = (index+shift) % len(alpha)
                outputMessage += alphaUpper[indexShifted]
    print(outputMessage)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt \n")
validOptions = ["encode", "decode"]
if direction not in validOptions:
    print(f"{direction} is not a valid Choice.")
else:
    shift = int(input("What is the value of shift? Please enter an integer \n"))
    message = input(f"What message would you like to {"send" if direction == "encode" else "receive"}? \n")

caesar(direction, message, shift)