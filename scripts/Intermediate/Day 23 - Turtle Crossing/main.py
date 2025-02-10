from car import CarManager
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from player import Player
import time 


# Set Up Screen
scr = Screen()
scr.setup(600, 600)
scr.colormode(255)
scr.listen()
scr.tracer(0)

# Init game objects
score = Scoreboard()
turt = Player()
cars = CarManager()

scr.onkeypress(key="Up", fun=turt.move)

game_on = True
while game_on:
    time.sleep(.1)
    scr.update()
    cars.spawn_car()
    # Detect collision with car
    for car in cars.cars:
        cars.drive()
        if car.distance(turt) < 20:
            score.game_over()
            game_on = False

    # Detect Finish Line
    if turt.ycor() > 250:
        turt.next_level()
        score.next_level()
scr.exitonclick()
