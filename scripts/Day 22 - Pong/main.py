from paddle import Paddle
from turtle import Turtle, Screen
from ball import Ball
from scoreboard import Scoreboard
PLAYER_ONE_XCOR = -350
PLAYER_TWO_XCOR = 350

boundary = Turtle()
score = Scoreboard()
scr = Screen()
scr.title("PONG")
scr.setup(width=800, height=600)
scr.bgcolor("black")
p1 = Paddle(PLAYER_ONE_XCOR)
p2 = Paddle(PLAYER_TWO_XCOR)
ball = Ball()
scr.listen()
scr.tracer(0)
scr.onkeypress(key="Up", fun=p2.move_up)
scr.onkeypress(key="Down", fun=p2.move_down)
scr.onkeypress(key="w", fun=p1.move_up)
scr.onkeypress(key="s", fun=p1.move_down)
game_on = True
while game_on:
    scr.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290: # Collision with top or bottom wall
        ball.bounce_y()
    if (ball.distance(p2) < 50 and ball.xcor() > 340) or (ball.distance(p1) < 50 and ball.xcor() < -340): # Collision with paddles
        ball.speed_up()
        ball.bounce_x()
    elif ball.xcor() > 340:
        # Player 1 scores
        print("point to player 1")
        ball.reset()
        score.increment_p1_score()
        # game_on = False 
    elif ball.xcor() < -340 :
        #Player 2 scores
        print("point to player 2")
        ball.reset() 
        score.increment_p2_score()
scr.exitonclick()