# Determines whether a tider is tall enough to ride a rollercoaster or not
print("Welcome to the rollercoaster!")
totalPrice = 0
height = int(input("Whas is your height in cm?"))
if height >= 120: # If 120 cm or taller, good to go
    print("You are tall enough to ride!")
    age = int(input("How old are you?"))
    if age <= 12:
        totalPrice = 5
        print("Child tickets are $5")
    elif age <= 18:
        totalPrice = 7
        print("Teen tickers are $7")
    elif age >=45 and age <= 55:
        print("Your ticket is free, go buy a sports car.")
    else:
        totalPrice = 12
        print("Adult tickets are $12")
        
    wantsPicture = input("Would you like a photo? y/n")
    if wantsPicture == "y":
        totalPrice += 3

    print(f"Your final bill is ${totalPrice}")
else: # Too short
    print("Sorry, you aren't tall enough to ride this ride.")
