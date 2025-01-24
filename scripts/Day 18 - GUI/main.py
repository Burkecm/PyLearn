###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import random as rand
from turtle import Turtle, Screen

def draw_square():
    for i in range(1,5):
        turt.forward(100)
        turt.right(90)

def draw_dotted_line():
    for i in range(1,5):
        turt.forward(10)
        turt.up()
        turt.forward(10)
        turt.down()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(1, num_sides+1):
        turt.forward(100)
        turt.right(angle)

def random_walk():
    directions = [0, 90, 180, 270]
    for _ in range(1, 100):
        turt.color(random_color())
        turt.setheading(rand.choice(directions)) 
        turt.forward(50)

def spirograph(turn_angle):
    turt.width(1)
    for _ in range(1, int(360 / turn_angle)):
        turt.color(random_color())
        turt.circle(100)
        turt.setheading(int(turt.heading()) + turn_angle)
        
def extract_colors(number_of_colors):        
    rgb_colors = []
    colors = colorgram.extract("scripts\Day 18 - GUI\image.jpg", number_of_colors)
    for color in colors:
        rgb_colors.append(color.rgb)

    return rgb_colors

def random_color():
    return rand.choice(extracted_colors)

def draw_dot(radius):
    turt.dot(radius, random_color())

def draw_row_of_dots(how_many, radius, gap):
    for _ in range(1, how_many+1):
        draw_dot(radius)
        turt.teleport(turt.pos()[0] + gap, turt.pos()[1])   

def draw_hirst_painting(rows, columns, gap, dot_radius):
    turt.teleport(-200, -200)
    start = turt.pos()
    for i in range(1, rows+1):
        draw_row_of_dots(columns, 20, 50)
        turt.teleport(start[0], start[1]+(50* i))

extracted_colors = extract_colors(30)
turt = Turtle()
turt.shape("turtle")
turt.speed("fastest")
turt.hideturtle()
screen = Screen()
screen.colormode(255)
draw_square()
draw_dotted_line()
for sides in range(3,11):
    color = random_color()
    turt.color(color.r, color.g, color.b)
    draw_shape(sides)
random_walk()
spirograph(5)
draw_hirst_painting(rows = 10, columns = 10, gap = 50, dot_radius = 20)

screen.exitonclick()
    