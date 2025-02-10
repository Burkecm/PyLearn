# List Comprehension
# new_list = [new_item for item in list]
import random as rand
import pandas
list = [1, 2, 3, 4, 5]
new_list = [n+1 for n in list]
print(new_list)

# conditional comprehension
# new_list = [n for n in list if condition]
names = ["Chabi", "Caroline", "Kevin", "Val", "Estre", "Mujen"]
c_names = [name.upper() for name in names if name[0]=="C"]
print(c_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number*number for number in numbers]
print(squared_numbers)

# Dictionary Comprehension
#dict = {new_key:new_value for (key, value) in dict.items()
dict = {"key1": "value1",
        "key2": "value2",
        "key3": "value3",
        "key4": "value4",
        }

student_scores = {student:rand.randint(0, 100) for student in names}
print(student_scores)

passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
result = {word:len(word)for word in words}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
def temp_c_to_f(temp_c):
        return (temp_c * 9/5) + 32
weather_f = {day:temp_c_to_f(temp_c) for (day, temp_c) in weather_c.items()}

print(weather_f)

# Iterating over a Panda df
student_dict = {
        "student": ["Reiwin", "Taj", "Isko", "Qudara"],
        "score": [40, 80, 41, 42] 
}

student_df = pandas.DataFrame(student_dict)
print(student_df)
for (key, val) in student_df.items():
        print(val)

for (index, row) in student_df.iterrows():
        print(row.student)

