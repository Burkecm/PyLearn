# # import csv

# # with open("scripts\Day 25 - Pandas\weather_data.csv") as weather:
# #     data = csv.reader(weather)
# #     temps = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temps.append(int(row[1]))
# #         print(row)

# #     print(temps)

# import pandas
# data = pandas.read_csv("scripts\Day 25 - Pandas\weather_data.csv")
# # print(type(data))
# # temp_series = data.temp

# # data_dict = data.to_dict()
# # print(data_dict)

# # temp_list = temp_series.tolist()
# # print(temp_list)
# # avg_temp = temp_series.mean()
# # print(avg_temp)
# # max_temp = temp_series.max()
# # print(max_temp)

# # # Get Row
# monday = data[data.day == "Monday"]
# print(monday)

# # hottest_day = data[data.temp == max_temp]
# # print(hottest_day)

# monday_temp_f = (9/5)*monday.temp[0] +32
# print(monday_temp_f)

import pandas
data = pandas.read_csv("scripts\Day 25 - Pandas\Squirrels\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_dct = {}
squirrel_dct["Fur Color"] = data["Primary Fur Color"].unique().tolist()[1:]
counts = []
for color in squirrel_dct["Fur Color"]:
    matches = len(data[data["Primary Fur Color"] == color])
    counts.append(matches)

squirrel_dct["Count"] = counts
squirrels = pandas.DataFrame(squirrel_dct)
squirrels.to_csv("scripts\Day 25 - Pandas\Squirrels\\squirrel_count.csv")