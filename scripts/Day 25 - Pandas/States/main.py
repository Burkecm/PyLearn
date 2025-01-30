from turtle import Turtle, Screen
import pandas
map = Turtle()
map_writer = Turtle(visible=False)
scr = Screen()

img = "scripts\\Day 25 - Pandas\States\\blank_states_img.gif"
scr.addshape(img)
map.shape(img)
def display_state(name, coords):
    map_writer.penup()
    map_writer.goto(coords)
    map_writer.write(name)

def generate_missed_states(filename):
    missed_states = []
    for state in states:
        if state not in guessed_states:
            missed_states.append(state)
    (pandas.DataFrame(missed_states)).to_csv(filename)

scr.title("Guess the States")
state_data = pandas.read_csv("scripts\\Day 25 - Pandas\States\\50_states.csv")
states = state_data.state.tolist()

# def get_click_coords(x, y):
#     print(x, y)
# scr.onscreenclick(get_click_coords)
game_over = False
correct_guesses = 0
guessed_states = []
while not game_over:
    guess = scr.textinput(f"Guess the states: {len(guessed_states)}/50!", "Go on, Guess!")
    if guess is None or guess.title() == "Quit":
        generate_missed_states("scripts\\Day 25 - Pandas\States\\missed_states.txt")
        game_over = True
    elif guess.title() in guessed_states:
        print("You've already got that one!")
    elif guess.title() in states:
        guessed_states.append(guess.title())
        coords = (state_data[state_data.state == guess.title()].x.tolist()[0], state_data[state_data.state == guess.title()].y.tolist()[0])
        display_state(guess, coords)
    else:
        print("That's Not a state, silly!")
scr.mainloop()