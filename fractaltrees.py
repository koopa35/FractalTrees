import turtle


#Turtle Set Up with Window Set Up
window = turtle.Screen()
window.bgcolor("white")
window.title("Fractal Tree")
pen = turtle.Turtle()



def branch(ITTERATION):
    pen.down()
    pen.forward(100/ITTERATION)
    pen.up()




#Puts the pen in the starting positon
pen.speed(1)
pen.up()
pen.left(90)
pen.goto(0,-340)

branch(1)

turtle.done()