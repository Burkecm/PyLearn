import random as rand
ranks = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # Ace, 2-10, J, Q, K
def hit():
    return rand.choice(ranks)

def playerTurn():
    choice = ""
    while choice != 'n': # Stay passes turn to dealer
        # Player may hit or stay
        choice = input(f"Your hand is {playerHand}. Would you like to hit (y) or stay(n)?\n")
        if choice == 'y': # Hit gives player another card
            playerHand.append(hit())
        playerScore = calcScore(playerHand)
        print(f"You have: {playerHand}")
        if playerScore > 21:
            print("BUST!")
            return True
    return False

def dealerTurn():
    # Dealer hits until sum(dealerHand) > 17
    dealerScore = calcScore(dealerHand)
    while dealerScore < 17:
        print(dealerScore)
        dealerHand.append(hit())
        dealerScore = calcScore(dealerHand)
        print(f"Dealer has: {dealerHand}")
        if dealerScore > 21:
            print("Dealer Busts!")
            return True
    return False

def DidIWin(player, dealer):
    if dealer == 0 or player > 21:
        return False
    elif player <= dealer and dealer <= 21:
        return False
    else:
        return True
    
def calcScore(hand):
    """Calculates sum of hand ranks, adjusting for duality of aces"""
    score = sum(hand)
    if hand.count == 2 and score == 21:
        return 0
    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

# Draw 2 hands of 2, one for each the player and Dealer
playerHand = [hit(), hit()]
playerScore = calcScore(playerHand)
dealerHand = [hit(), hit()]
dealerScore = calcScore(dealerHand)
gameover = False
bust = False
# Check for blackjacks
if calcScore(dealerHand) == 0: # dealer has blackjack
    print(f"Dealer has {dealerHand}: Dealer has Black Jack. You Lose.")
    gameover = True
elif calcScore(playerHand) == 0:
    print(f"You have {playerHand}: Blackjack! You Win!")
    gameover = True

# No Blackjacks, proceed with game. 
print(f"Dealer's first card: {dealerHand[0]}")
# Player's Turn
while not gameover:
    #Player Turn
    choice = input(f"You have {playerHand}. Would you like to hit (y) or stay(n)?\n")
    if choice == "y":
        playerHand.append(hit())
        playerScore = calcScore(playerHand)
        if playerScore > 21:
            gameover = True
    elif choice == "n":
        gameover = True
        playerScore = calcScore(playerHand)
    print(f"You have: {playerHand} for a score of {playerScore}")
    if playerScore > 21:
        print("You Bust! Womp Womp")
        bust == True

# Proceed to Dealer Turn
print(dealerHand)
while dealerScore < 17 and not bust and dealerScore != 0:
    dealerHand.append(hit())
    dealerScore = calcScore(dealerHand)
    print(f"Dealer hits! {dealerHand}")
if DidIWin(playerScore, dealerScore):
    print(f"Your hand is {playerHand} for a score of {playerScore}. The House has {dealerScore}. YOU WIN!")
else:
    print(f"Your hand is {playerHand} for a score of {playerScore}.The House has {dealerScore}. Better Luck next time!")





# playerBust = playerTurn()
# dealerBust = False
# if not playerBust:
#     dealerBust = dealerTurn()


# If dealer busts or playerScore > dealerScore, Player wins, else dealer wins
# if dealerBust or (not playerBust and playerScore > dealerScore):
#     print(f"You Win with {playerScore}! Dealer has {dealerScore}")
# else:
#     print(f"You Lose. Dealer wins with {dealerScore}. You had {"BUST" if playerBust else playerScore}")
