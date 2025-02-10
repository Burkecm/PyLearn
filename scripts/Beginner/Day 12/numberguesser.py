import random as rand

def didIWin(guess, target):
    if guess < target:
        print("Higher!")
        return False
    elif guess > target:
        print("Lower!")
        return False
    if guess == target:
        return True

gameover = False
while not gameover:
    hardMode = False
    guesses = 10
    correct = False
    numbertoGuess = rand.randint(1, 100)
    print("I'm thinking of a number between 1 and 100! Can you guess what it is? I'll give you hints\n")
    if input(f"Would you like to play on easy mode or hard mode?\n") == "hard":
        hardMode = True
        guesses = 5

    while not correct and guesses > 0:
        guess = int(input(f"You have {guesses} guesses remaining. \nGuess a number! \n"))
        correct = didIWin(guess, numbertoGuess)
        if not correct:
            guesses -= 1

    if guesses > 0:
        if input(f"You got it! the number was {guess}! Would you like to play again?\n") != "y":
            gameover = True
    else: 
        if input(f"Sorry, you didn't get it. The number was {numbertoGuess}. Would you like to try again? y/n\n") != "y":
            gameover = True