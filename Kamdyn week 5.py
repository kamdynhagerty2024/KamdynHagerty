#Name: Section4.9Problem2
#Purpose: Squares
#Author: KamdynHagerty
#Created: 2/17/26

import turtle

screen = turtle.Screen()
screen.bgcolor("green") 
alex = turtle.Turtle()
alex.speed(0)  
alex.color("pink")  
alex.fillcolor("")
size = 20
num_squares = 5

for i in range(num_squares):
    alex.penup()
    alex.goto(-size/2, -size/2)
    alex.pendown()
    for _ in range(4):
        alex.forward(size)
        alex.left(90)
    size += 20


