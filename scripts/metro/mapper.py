from turtle import Turtle, Screen
from station import Station
import random as rand
mapper = Turtle() 

class SubwayMap(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)        
        self.stations = {"start": Station(coords=self.generate_random_location()), "end": Station(coords=self.generate_random_location())}
        self.label_start_end()
        self.next_stop = 1
        print(self.stations)

    def draw_station(self, x, y):
        self.stations[str(self.next_stop)] = Station((100 * round(x/100), 100 * round(y/100)))
        self.next_stop += 1
        print(self.stations)
    
    def draw_yaxs(self, gridsize):
        for i in range(11):
            mapper.forward(1000)
            mapper.teleport(-500+(gridsize*i), -500)

    def draw_xaxs(self, gridsize):
        for i in range(11):
            mapper.forward(1000)
            mapper.teleport(-500, -500+(gridsize*i))
    
    def draw_grid(self, gridsize):
        mapper.speed(100)
        mapper.teleport(-500, -500)
        mapper.left(90) 
        self.draw_yaxs(gridsize)
        mapper.right(90)
        mapper.teleport(-500, -500)
        self.draw_xaxs(gridsize)
        mapper.teleport(-500, -500)
        mapper.forward(1000)
        mapper.left(90)
        mapper.forward(1000)
        mapper.left(90)
        mapper.forward(1000)
        mapper.left(90)
        mapper.hideturtle()

    def label_start_end(self):
        mapper.teleport(self.stations["start"].pos()[0]+10, self.stations["start"].pos()[1]+10)
        mapper.write("Start")
        mapper.teleport(self.stations["end"].pos()[0]+10, self.stations["end"].pos()[1]+10)
        mapper.write("End")
    
    def generate_random_location(self):
        x = 100 * round((rand.randint(-500, 500)/100))
        y = 100 * round((rand.randint(-500, 500)/100))
        return (x, y)