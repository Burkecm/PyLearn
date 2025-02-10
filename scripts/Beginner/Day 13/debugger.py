import random as rand
import math as math

def mutate(aList):
    bList = []
    newItem = 0
    for item in aList:
        newItem = item * 2
        newItem += rand.randint(1, 3)
        newItem = newItem +item
    # bList.append(newItem)
        bList.append(newItem)
    print(bList)

mutate([1, 2, 3, 5, 6, 13])

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
print(is_leap(2300))

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print(number)

fizz_buzz(15)