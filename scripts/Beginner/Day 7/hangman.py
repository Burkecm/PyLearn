import random as rand
wordsList = ["aardvark", "baboon", "camel"]


# Randomly decide which word user is guessing
wordToGuess = list(rand.choice(wordsList))
#print(wordToGuess)
#print("".join(wordToGuess))

#Generate a string of blanks to represent unguessed letters. 
blanks = ""
for letter in wordToGuess:
    blanks += "_"
print(blanks)

# Ask the user to guess a letter and assign to var guess. Make Lowercase
gameOver = False
correctLetters = []
numLives = 6
while not gameOver:
    print(f"Lives Left: {numLives} / 6")
    guess = input("Guess a letter: ").lower()
    if guess not in wordToGuess:
        numLives -= 1
    if numLives == 0:
        gameOver = True
        print("You Lose!")

    if guess in correctLetters:
        print(f"You've already guessed {guess}!")
    # Check if guess is in word. Display aggregated guesses
    display = ""
    for letter in wordToGuess:
        if letter == guess:
            display += letter
            correctLetters.append(letter)
        elif letter in correctLetters:
            display+= letter       
        else:
            display += "_"
    currentGuess = display
    print(display)

    if "_" not in display:
        gameOver = True
        print("You Win!")
