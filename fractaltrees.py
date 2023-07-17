import turtle

#Turtle Set Up with Window Set Up
window = turtle.Screen()
window.bgcolor("white")
window.title("Fractal Tree")
window.colormode(255)
pen = turtle.Turtle()
pen.speed(0)

#Branches variable is how many recursive branches deep the tree goes
BRANCHES = int(input("Enter a Number of Branches: "))
def branch(ITTERATION):
    if ITTERATION < BRANCHES:
        pen.color(0, 0, 0 + (255//BRANCHES)*ITTERATION)
        #Left Branch
        pen.down()
        POS = pen.position()
        pen.left(25)
        HEAD = pen.heading()
        pen.forward(100/ITTERATION)
        branch(ITTERATION + 1)
        
        #Reset
        pen.up()
        pen.setposition(POS)
        pen.setheading(HEAD)
        pen.color(0, 0, 0 + (255//BRANCHES)*ITTERATION)

        
        #Right Branch
        pen.right(50)
        pen.down()
        pen.forward(100/ITTERATION)
        branch(ITTERATION + 1)

#Puts the pen in the starting positon
pen.color(0, 0, (255//BRANCHES))
pen.up()
pen.left(90)
pen.setposition(0,-500)
pen.down()
pen.forward(200)

ITTERATIONS = 1
branch(ITTERATIONS)

turtle.done()