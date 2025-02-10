from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self, shape = "circle", ):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.x_heading = 1
        self.y_heading = 1
        self.move_speed = .01

    def move(self):
        time.sleep(self.move_speed)
        self.goto(self.xcor()+self.x_heading, self.ycor()+self.y_heading)

    def bounce_y(self):
        self.y_heading *= -1

    def bounce_x(self):
        self.x_heading *= -1

    def reset(self):
        self.teleport(0, 0)
        self.bounce_x()
        self.move_speed = .01

    def speed_up(self):
        self.move_speed *= .7