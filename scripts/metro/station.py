from turtle import Turtle
import random as rand
class Station(Turtle):
    def __init__(self, coords, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.coords = coords
        self.teleport(*self.coords)
        self.dot(20)
