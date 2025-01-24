# Class declarations
# # PascalCase Names
# import turtle as turt 
# from turtle import Turtle as Turt, Screen
from prettytable import PrettyTable 

# yurtle = Turt()
# yurtle.shape("turtle")
# yurtle.color("green")
# yurtle.forward(100)
# yurtle.circle(40)
# yurtle.forward(100)
# #print(yurtle)
# screen = Screen()
# #print(screen.canvheight)
# screen.exitonclick()
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur"])
table.add_column("Type", ["Electric", "Water", "Fire", "Grass"])
table.align = "l"
print(table)