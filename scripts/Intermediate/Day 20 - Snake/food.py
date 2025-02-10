from turtle import Turtle
import random as rand

class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.color("blue")
        self.shapesize(.5, .5)
        self.speed("fastest")
        self.teleport(rand.randint(-280, 280), rand.randint(-280, 280))

    def reset(self):
        self.teleport(rand.randint(-280, 280), rand.randint(-280, 280))