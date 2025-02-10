

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Cannot divide by Zero")
        return 0
    return a / b

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide
              }
def calculator():    
    # Input a number
    n1 = float(input("What is the first number?: "))

    continueYN = "y"
    while continueYN == "y":
        # input an operation
        op = input("Which operation would you like to perform?")
        if op not in operations:
            print("Invalid Operation. Quitting.")
            return
        # Input a second number
        n2 = float(input("What is the second number?: "))
        result = operations[op](n1, n2)
        print(f"{n1} {op} {n2} = {result}")

        # Choose y/n - if y: ask for an operation and second number. If n: begin new calculation 
        continueYN = input("Would you like to continue (y) or begin a new operation (n)? \n")
        if continueYN == 'y':    
            n1 = result
        elif continueYN == 'n':
            calculator()

calculator()