from turtle import Turtle
import random as rand
class Station(Turtle):
    def __init__(self, coords, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.coords = coords
        self.teleport(*self.coords)
        self.dot(20)
        self.stop_number = 1
        # self.label()

    # def generate_starting_location(self):
    #     x = 100 * round((rand.randint(-500, 500)/100))
    #     y = 100 * round((rand.randint(-500, 500)/100))
    #     return (x, y)
    
    # def draw(self):
    #     self.