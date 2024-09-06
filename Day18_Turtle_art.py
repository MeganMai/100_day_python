import random
import turtle
import colorgram 

from turtle import Turtle, Screen
tim = Turtle()
turtle.colormode(255)
directions = [0,90,180,270]
#tim.pensize(15)
tim.speed('fastest')
colors = colorgram.extract('dotimage.jpg',100)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
def move(steps):
    tim.penup()
    tim.forward(steps)
    tim.pendown()
tim.setheading(225)
move(300)
tim.setheading(0)
w = 20
h = 20
for i in range (w):
    for j in range (h):
        tim.dot(10)
        tim.color(random.choice(rgb_colors))
        if (j == h-1) and (i%2 ==0):
            tim.setheading(90)
            move(20)
            tim.setheading(180)
        elif (j == h-1) and (i%2 != 0):
            tim.setheading(90)
            move(20)
            tim.setheading(0)
        else: 
            move(20)
    

screen = Screen()
screen.exitonclick()

