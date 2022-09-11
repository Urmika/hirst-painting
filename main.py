# import colorgram
# l =[]
# colors = colorgram.extract('img.jpg',12)
# for col in colors:
#
#     rgb = col.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     t = (r,g,b)
#     l.append(t)
#
# print(l)
import turtle
from turtle import Turtle,Screen
from random import choice
turtle.colormode(255)
colour_list = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16)]
tim = Turtle()
tim.speed("fastest")
a = 0
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for i in range (10):
    for j in range(10):
        tim.dot(20,choice(colour_list))
        tim.penup()
        tim.forward(50)
        #tim.pendown()
        #j +=1

    #tim.penup()
    tim.setheading(90)
    tim.fd(50)
    tim.seth(180)
    tim.fd(500)
    tim.seth(0)

   # i+=1




screen = Screen()
screen.exitonclick()