with open("scripts\Day 24 - Filepaths\input\\names\invited_names.txt") as nam:
    names = nam.readlines()

for name in names:
    with open("scripts\Day 24 - Filepaths\input\letters\starting_letter.txt") as let:
        letter = let.read()
    letter = letter.replace("[name]", name.strip())
    with open(f"scripts\Day 24 - Filepaths\output\\ready_to_send\\{name.strip()}.txt", "w") as invite:
        invite.write(letter)