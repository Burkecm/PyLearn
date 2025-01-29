from turtle import Turtle
import random as rand
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


def random_color():
    return rand.choice(COLORS)

class CarManager:
    def __init__(self):
        self.cars = []
        self.level = 1
        self.move_speed = .03


    def drive(self):
        time.sleep(self.move_speed)
        for car in self.cars:
            car.forward(10)

    def spawn_car(self):
        if rand.randint(1, 6) == 6:
            car = Turtle()
            car.shape("square")
            car.color(random_color())
            car.shapesize(1, 2)
            car.penup()
            car.setheading(180)
            car.teleport(300, rand.randint(-250, 250))
            self.cars.append(car)

    def next_level(self):
        self.move_speed += .01