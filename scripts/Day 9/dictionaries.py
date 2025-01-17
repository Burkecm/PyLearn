progDict = {"bug": "An erorr in a program",
            "function": "Chunk of code easily called multiple times",
            }

#  get value by key
print(progDict["function"])

# addto /update a dictionary
progDict["loop"] = "The action of doing something over and over again"

print(progDict)

# Declare empty dict
emptyDict = {}

# clear existing dict
# progDict = {}
# print(progDict)

# loop through a dict
for key in progDict:
    print(f"{key}: {progDict[key]}")


student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif 81 <= student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 71 <= student_scores[key] <= 80:
        student_grades[key] = "Acceptible"
    elif student_scores[key] <= 70:
        student_grades[key] = "Fail"
    else:
        student_grades[key] = "TBD"
print(student_grades)

# Nesting dicts/lists
capitals = {"France": "Paris",
           "Germany": "Berlin"}

travelLog = {"France": ["Paris", "Lille", "Nice"],
             "Germany":["Stuttgart", "Berlin"]}
print(travelLog["France"][1])

travelLog = {
    "France":{
        "num_visits": 8,
        "citiesVisited": ["Paris", "Lille", "Nice"]
    },
    "Germany": {
        "num_visits": 4,
        "citiesVisited": ["Stuttgart", "Berlin"]
    }
}
print(travelLog["France"]["citiesVisited"][1])
