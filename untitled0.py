# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:44:43 2022

@author: KIIT
"""

import turtle as turtle
color=["red","purple","blue","green","orange","yellow"]
cursor=turtle.pen()
turtle.speed(59)
turtle.bgcolor("black")
for i in range(360):
    turtle.pencolor(color[i%6])
    turtle.width(i/100+1)
    turtle.forward(i)
    turtle.left(59)
turtle.hideturtle()
turtle.done()