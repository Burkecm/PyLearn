def myFunc(a, b):
    return a * b

print(myFunc(2, 3))

def formatName(firstname, lastname):
    # Docstring
    """Take first and last name and format it to return the 
    names concatenated in title case"""
    # firstname = firstname[0].upper() + firstname[1:]
    # lastname = lastname[0].upper() + lastname[1:]
    # return f"{firstname[0].upper() + firstname[1:]} {lastname}"
    return f"{firstname} {lastname}".title()

print(formatName("chad", "burke"))

def is_leap_year(year):
    """Determines whether the given year is a leap year or not. """
    if year % 400 == 0 :
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
        
print(is_leap_year(800)) # True
print(is_leap_year(850)) # False
print(is_leap_year(200)) # False
print(is_leap_year(80))  # True

# Docstring