# First day of CSC1301 for python
 # Jonathan Deaton

import turtle
    # Turtle graphics

t = turtle.Turtle()
t.speed(0)
# 10 is fastest, 0 can make it show no animation
# Establishes variable t to recall
t.color("yellow")
# any color put under quotations

t.width(3)
# width or pensize

for x in range(200):
    t.forward(x*2)
# Recalling the x value that was established as the range 200
    t.left(95)
# Left 90 degrees repeated 200 times

input("Press ENTER to Exit")
# Requires the input ENTER to exit python code

