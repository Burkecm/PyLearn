from turtle import Turtle, Screen 
import random as rand
turt = Turtle("turtle")
scr = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
starting_positions = [80, 50, 20, -10, -40, -70, -100]
turts = []
# # Etch-a-Sketch
# def move_forward():
#     turt.forward(10)

# def turn_right():
#     turt.right(10)

# def turn_left():
#     turt.left(10)

# def reverse():
#     turt.backward(10)

# def clear():
#     turt.teleport(0, 0)
#     scr.reset()

# # Listener Events
# scr.listen()
# scr.onkey(key="c", fun=clear)
# scr.onkeypress(key="w", fun=move_forward)
# scr.onkeypress(key="d", fun=turn_right)
# scr.onkeypress(key="a", fun=turn_left)
# scr.onkeypress(key="s", fun=reverse)

def random_distance():
    return rand.randint(0, 10)

# Turtle Race
scr.setup(width = 500, height = 400)
race = False
user_bet = scr.textinput(title="Place Your Bet!", prompt="Who will win? Enter a color: ")
winner = ""

if user_bet not in colors:
    print("That turtle is not in this race.")
else:
    race = True
    for turtle_index in range(0, 7):
        turt = Turtle("turtle")
        turt.color(colors[turtle_index])
        turt.up()
        turt.goto(-230, starting_positions[turtle_index])
        turt.down()
        turts.append(turt)

while race:
    for t in turts:
        t.forward(random_distance())
        print(t.pos())
    if t.xcor() > 200:
        race = False
        winner = t.pencolor()
        if winner == user_bet:
            print("You Win!")
        else:
            print(f"Sorry, you lose, the {winner} turtle won.")

scr.exitonclick()
