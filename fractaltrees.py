import turtle

'''
Fractal Tree Drawer in a window with user input for number of recursive
branch itterations as well as 2-dimensional color mapping through the
use of itterative color maps. This program is written by Connor Powell,
and its git hub repo is: https://github.com/koopa35/FractalTrees
'''

#################
#BRANCH FUNCTION#
#################
def branch(ITTERATION):
    if ITTERATION < BRANCHES:
        #Left Branch
        pen.color(255 - 255//BRANCHES*ITTERATION*(1-int(RED)),
                   255 - 255//BRANCHES*ITTERATION*(1-int(GREEN)),
                     255 - 255//BRANCHES*ITTERATION*(1-int(BLUE)))
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
        pen.color(255 - 255//BRANCHES*ITTERATION*(1-int(RED)),
                   255 - 255//BRANCHES*ITTERATION*(1-int(GREEN)),
                     255 - 255//BRANCHES*ITTERATION*(1-int(BLUE)))
        
        #Right Branch
        pen.right(50)
        pen.down()
        pen.forward(100/ITTERATION)
        branch(ITTERATION + 1)


########################
#COLOR DISPLAY FUNCTION#
########################
def colordisp(RED, GREEN, BLUE):
    pen.up()
    pen.color("RED")
    pen.setposition(-600, 500)
    pen.down()
    pen.write("RED: " + RED, font=("Verdana",20, "normal"))

    pen.up()
    pen.color("GREEN")
    pen.setposition(-600, 450)
    pen.down()
    pen.write("GREEN: " + GREEN, font=("Verdana",20, "normal"))

    pen.up()
    pen.color("BLUE")
    pen.setposition(-600, 400)
    pen.down()
    pen.write("BLUE: " + BLUE, font=("Verdana",20, "normal"))

    pen.up()
    pen.color("GRAY")
    pen.setposition(350, -525)
    pen.down()
    pen.write("By: Connor Powell", font=("Verdana",20, "normal"))


#SETUP
#####################################################################################
#Turtle Set Up with Window Set Up
window = turtle.Screen()
window.bgcolor("black")
window.title("Fractal Tree")
window.colormode(255)
pen = turtle.Turtle()
pen.speed(0)

#User input Branches variable is how many recursive branches deep the tree goes
BRANCHES = int(input("Enter a Number of Branches: "))
#Takes User input for color
COLORS = input("INPUT RGB VALUES 1 or 0: ")
RED, GREEN, BLUE = COLORS.split()

#Puts the pen in the starting positon
colordisp(RED, GREEN, BLUE)
pen.color(255, 255, 255)
pen.up()
pen.left(90)
pen.setposition(0,-500)
pen.down()
pen.forward(200)
#####################################################################################

#FUNCTION CALL 
ITTERATIONS = 1
branch(ITTERATIONS)
turtle.done()
