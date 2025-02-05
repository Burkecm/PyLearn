from turtle import Turtle, Screen
from mapper import SubwayMap
def draw_station(x, y):
    subway_map.draw_station(x, y)
    scr.update()

subway_map = SubwayMap()
turt = Turtle()
turt.hideturtle()
scr = Screen()
scr.setup(1100, 1100)
scr.tracer(0)
scr.listen()
subway_map.draw_grid(gridsize=100)
scr.update()
scr.onscreenclick(draw_station)                  
scr.mainloop()


