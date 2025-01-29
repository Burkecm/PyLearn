# with open("scripts\Day 24 - Filepaths\myfile.txt") as file:
#     contents = file.read()
#     print(contents)

with open("scripts\Day 24 - Filepaths\myfile.txt", mode="a") as file:
    file.write("\nHello World!\n")

with open("scripts\Day 24 - Filepaths\\newFile.txt", mode = 'w') as file:
    file.write("I'm hew in town")