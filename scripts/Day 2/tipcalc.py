# Calculates how to split a bill with given subtotal, tip percentage, and ways to split
print("Welcome to he tip calculator!")
subtotal = float(input("What was the total bill? $"))
tip =   int(input("What perent would you like to tip?"))
split = int(input("How many people to split the bill?") )
total = round((subtotal * (1+(tip/100)))/split, 2)
print(f"Each person should pay ${total}")