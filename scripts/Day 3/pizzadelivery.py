print("Welcome to Panucci Python's Pizza! COME ONNNNN!!!")
totalBill = 0
size = input("What size pie you want?, S, M, or L: ")
# S: $15, M: $20, L: $25
if size == "S":
    totalBill = 15
elif size == "M":
    totalBill = 20
elif size == "L":
    totalBill = 25

pep = input("You want some pepperoni cups? Y/N: ")
# Pep costs $2 for Small, $3 for Med/Large
if pep == "Y":
    if size == "S":
        totalBill += 2
    else:
        totalBill += 3

extraCheese = input("You want extra cheese? Y/N: ")
# Extra Cheese costs $1
if extraCheese == "Y":
    totalBill += 1

print(f"Your total comes to ${totalBill}, COME ONNNNNN!")