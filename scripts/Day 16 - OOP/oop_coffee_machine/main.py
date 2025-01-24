from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable

def print_menu(Menu):
    table_menu = PrettyTable()
    drinks = menu.get_items().split("/")
    if drinks[-1] == "":
        drinks.pop() # Remove trailing empty item from ending "/"
    table_menu.add_column("Drink", drinks)
    prices = []
    for d in drinks:
        prices.append(menu.find_drink(d).cost)
        
    table_menu.add_column("Price", prices)
    print(table_menu)

def print_functions():
    table_functions = PrettyTable()
    choiceValid = False
    buttons = [1, 2, 3]
    table_functions.add_column("Button", buttons)
    table_functions.add_column("Operation", ["Print Report", "Order a Drink", "Turn Off Machine"])
    print(table_functions)
    while not choiceValid:
        choice =  int(input("Which button will you press? (enter number): \n"))
        if choice in buttons:
            return choice
        else: 
            print("Invalid Response")


# Instantiate Objects
cm = CoffeeMaker()
menu = Menu()
bank = MoneyMachine()
machine_off = False

while not machine_off:
    selected_function = print_functions()
    if selected_function == 1:
        cm.report()
        bank.report()
    elif selected_function == 2:
        # Present the menu
        print_menu(menu)

        # Take customer order
        choice = input("What kind of drink would you like?\n")
        drink = menu.find_drink(choice)

        # Gimme your money
        transaction_successful = bank.make_payment(drink.cost)

        # check machine for required incredients
        if cm.is_resource_sufficient(drink) and transaction_successful:
            cm.make_coffee(drink)
    elif selected_function == 3:
        machine_off = True
