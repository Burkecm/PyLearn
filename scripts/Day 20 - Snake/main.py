from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def game_over():
    score.reset()
    sneko.reset()
    food.reset()

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("SNAKE? SNAAAAAAAKE!")
scr.tracer(0)
sneko = Snake(3)
food = Food()
score = Scoreboard()

scr.listen()
scr.onkey(key="w", fun=sneko.up)
scr.onkey(key="a", fun=sneko.left)
scr.onkey(key="s", fun=sneko.down)
scr.onkey(key="d", fun=sneko.right)
scr.onkey(key="Up", fun=sneko.up)
scr.onkey(key="Left", fun=sneko.left)
scr.onkey(key="Down", fun=sneko.down)
scr.onkey(key="Right", fun=sneko.right)
game_on = True
while game_on:
    scr.update()
    time.sleep(.05)
    sneko.move_forward()

    # Detect Collisions
    if sneko.head.distance(food.pos()) < 15:
        print("omnomnom")
        food.reset()
        sneko.grow()
        score.increase_score()
    if  290 < sneko.head.xcor()  or sneko.head.xcor() < -290 or 290 < sneko.head.ycor()  or sneko.head.ycor() < -290: 
        game_over()

    for segment in sneko.body[1:]:
        # if segment != sneko.head:
            if sneko.head.distance(segment) < 10:
                game_over()
            
    
    
scr.exitonclick()