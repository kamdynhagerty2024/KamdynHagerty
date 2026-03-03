#Name: Section5.14problem8
#Purpose: Extracredit
#Author: KamdynHagerty
#Created: 2/17/26

import turtle

def draw_bar(t, height):
    if height >= 200:
        t.fillcolor("red")
    elif height >= 100:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")
    
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(height, align="center")
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
wn = turtle.Screen()
t = turtle.Turtle()

t.penup()
t.goto(-200, -200)
t.pendown()

data = [50, 120, 180, 220, 75, 250]

for value in data:
    draw_bar(t, value)






