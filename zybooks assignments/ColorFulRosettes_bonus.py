# Step by step notes #

# need to write an array of colors
# colors = [colors]
# highlight all of the range and indent it for the nest loop

# Start making the nest loop with a beginning for loop

# ColorfulRosettes.py
import turtle

t=turtle.Pen()
turtle.bgcolor('black')

t.speed(0)
t.width(3)
# colors in the array need to be all lowercase
colors = ["red", "orange", "yellow", "green", "orange", "blue","indigo", "violet"]
# Ask the user for the number of circles in their rosette, default to 6
number_of_circles = int(turtle.numinput("Number of circles",
                                        "How many circles in your rosette?", 6))
size = int(turtle.numinput("Circle Size", 
                                  "What size do you want your circle?", 50))


# for color in turtle graphics in the range colors that was established
for color in colors:
# color is now established so instead of trying to reference the list created above, it is now the word established in the for loop "color"
    t.pencolor(color)
    for x in range(number_of_circles):
        t.circle(size)
        t.left(360/number_of_circles)
    size -= 25


input()
