from turtle import Turtle, Screen
import random
tim = Turtle()
tim.color("black")
tim.shape("turtle")

# draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon
# each drawn with a random colour
# each side 100 in length


# number of sides
# colour
# angle
# length

def change_colour():
    R = random.random()
    B = random.random()
    G = random.random()
    return R, B, G

side_number = list(range(3,11))

for number in side_number:
    index = side_number.index(number)
    tim.color(change_colour())
    for _ in range(number):
        tim.forward(100)    
        angle = tim.right(360/(side_number[index]))
        

# move forward and turn left
# move forward and turn right
# move backward and turn left
# move backward and turn right

for _ in range (500):
    tim.pensize(10)
    tim.speed(0)
    tim.color(change_colour())
    options = [1, 2, 3, 4]
    decision = random.choice(options)

    if decision == 1:
        tim.forward(50)
       
    elif decision == 2:
        tim.right(90)
        tim.forward(50)

    elif decision == 3:
        tim.back(50)
        
    elif decision == 4:
        tim.left(90)
        tim.forward(50)

# radius 100 circles

tim.speed(0)

for _ in range (72):
    tim.color(change_colour())
    tim.circle(100)
    tim.left(5)















screen = Screen()
screen.exitonclick()











