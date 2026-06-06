import another_module
print(another_module.another_variable)


import turtle
timmy = turtle.Turtle() 
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
# Turtle is a class, and timmy is an instance of that class. 
# print(timmy)


# or
from turtle import Screen, Turtle
# timmy = Turtle()
# print(timmy)



my_screen = Screen()
my_screen.canvheight
# print(my_screen.canvheight)
my_screen.exitonclick()
# exitonclick is a method that will close the window when you click on it.
