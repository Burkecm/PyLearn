import random as rand
rps = ["Rock", "Paper", "Scissors"]
playerChoice = int(input("Which do you choose? 0: Rock, 1: Paper, 2: Scissors.\n"))

opponentChoice = rand.randint(0, 2)
print(f"Your opponent chose {rps[opponentChoice]}")
if playerChoice >= 3 or playerChoice < 0:
    print("Invalid Choice: You Lose")
elif playerChoice == opponentChoice:
    print("It's a draw!")
elif playerChoice == 0 and opponentChoice == 2:
    print("You Won!")
elif opponentChoice == 0 and playerChoice == 0:
    print("You Lose!")
elif playerChoice > opponentChoice:
    print("You Won!")
elif opponentChoice > playerChoice:
    print("You Lose!")
