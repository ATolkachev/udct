# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle

# Your code here.

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_figures():

    window = turtle.Screen()
    window.bgcolor("green")

#    bernie = turtle.Turtle()
#    bernie.forward(200)
#    bernie.right(90)
#    bernie.forward(200)
#    bernie.right(135)
#    bernie.forward(282.842712475)


    tim = turtle.Turtle()
    tim.speed(1)
    tim.color("black")
    tim.forward(100)
    tim.backward(50)
    tim.right(90)
    tim.forward(100)

    tim.up()

    tim.setpos(150, -100)
    tim.down()
    tim.left(180)
    tim.forward(100)
    tim.right(135)
    tim.forward(80)
    tim.left(90)
    tim.forward(80)
    tim.right(135)
    tim.forward(100)


    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color('red')
    brad.speed(10)
    for i in range(1,36):
        draw_square(brad)
        brad.right(10)

    angie = turtle.Turtle()
    angie.circle(100)
    angie.shape("arrow")
    angie.color("blue")

    window.exitonclick()

draw_figures()
