#Project 1
# Successfully completed all of Part 1
# Successfully completed all of Part 2
# Successfully completed stamps amd part of the random triangles in Part 3
import turtle
import math
import random

#Part 1- A fancy turtle boxtrot

def main():
    print("Project 1 by ShaLeah Wimby")
    draw_picture()
    
def draw_picture():
    window = turtle.Screen()
    AI = turtle.Turtle()
    Waba = turtle.Turtle()
    Q = turtle.Turtle()
    draw_2nd_border(Waba)
    draw_border(Waba)
    draw_triangle(Waba)
    perform_boxtrot(AI)
    draw_first_initial(AI)
    draw_last_initial(AI)
    stamp_1st_initial(Q)
    stamp_last_initial(Q)
    random_triangle_colors(Q)

def draw_filled_square(turtle, size, color):
    turtle.speed(0)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
    
def perform_boxtrot(turtle):
    turtle.up()
    turtle.goto(-220,320)
    turtle.down()
    draw_filled_square(turtle, 200, "pink")
    
    turtle.up()
    turtle.goto(-30,320)
    turtle.down()
    draw_filled_square(turtle, 200, "light blue")
    
    turtle.up()
    turtle.goto(-220,120)
    turtle.down()
    draw_filled_square(turtle, 200, "light blue")
    
    turtle.up()
    turtle.goto(-30,120)
    turtle.down()
    draw_filled_square(turtle, 200, "pink")
    
def draw_first_initial(turtle):
    turtle.up()
    turtle.goto(-130,250)
    turtle.width(5)
    turtle.down()
    turtle.left(180)
    for i in range(3):
        turtle.forward(30)
        turtle.left(90)
    turtle.right(180)
    for i in range(2):
       turtle.forward(30)
       turtle.right(90)
       
def draw_last_initial(turtle):
    turtle.up()
    turtle.goto(15, 50)
    turtle.width(5)
    turtle.down()
    turtle.right(180)
    turtle.left(25)
    turtle.forward(75)
    turtle.left(130)
    turtle.forward(50)
    turtle.right(90)
    turtle.right(25)
    turtle.forward(50)
    turtle.left(130)
    turtle.forward(75)
    
#Part 2- A matte, a frame of triangles, and a second turtle
def draw_border(turtle):
    turtle.up()
    turtle.goto(-250, 340)
    turtle.down()
    turtle.speed(0)
    draw_filled_square(turtle, 450, "gray")
    
def draw_2nd_border(turtle):
    turtle.up()
    turtle.goto(-300,390)
    turtle.down()
    turtle.speed(0)
    for i in range(4):
        turtle.forward(550)
        turtle.right(90)
    
def draw_triangle(turtle):
    turtle.up()
    turtle.goto(-300,390)
    turtle.down()
    for i in range(11):
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(135)
        turtle.forward(70.7)
        turtle.right(135)
        turtle.forward(50)
        turtle.end_fill()
        
    turtle.up()
    turtle.goto(-300,-110)
    turtle.down()
    for i in range(11):
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(135)
        turtle.forward(70.7)
        turtle.right(135)
        turtle.forward(50)
        turtle.end_fill()

    turtle.up()
    turtle.goto(-300,340)
    turtle.down()
    for i in range(9):
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(135)
        turtle.forward(70.7)
        turtle.left(135)
        turtle.forward(50.7)
        turtle.left(90)
        turtle.end_fill()
    
    turtle.up()
    turtle.goto(200,340)
    turtle.down()
    for i in range(9):
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(135)
        turtle.forward(70.7)
        turtle.left(135)
        turtle.forward(50.7)
        turtle.left(90)
        turtle.end_fill()
        
# Part 3- Stamped initials and random colors for the triangles
def stamp_1st_initial(turtle):
    turtle.speed(0)
    turtle.up()
    turtle.goto(-130,250)
    turtle.color("blue")
    turtle.shape("turtle")
    turtle.rt(180)
    for i in range(4):
        turtle.stamp()
        turtle.fd(7)
    turtle.rt(270)
    turtle.fd(5)
    for i in range(3):
        turtle.stamp()
        turtle.fd(7)
    turtle.lt(90)
    turtle.fd(5)
    for i in range(3):
        turtle.stamp()
        turtle.fd(7)
    turtle.rt(90)
    turtle.fd(5)
    for i in range(3):
        turtle.stamp()
        turtle.fd(7)
    turtle.rt(90)
    turtle.fd(5)
    for i in range(3):
        turtle.stamp()
        turtle.fd(7)
        
def stamp_last_initial(turtle):
    turtle.speed(0)
    turtle.up()
    turtle.goto(15,50)
    turtle.color("violet")
    turtle.shape("turtle")
    turtle.lt(115)
    for i in range(10):
        turtle.stamp()
        turtle.forward(7)
    turtle.left(130)
    for i in range(8):
        turtle.stamp()
        turtle.forward(6)
    turtle.right(115)
    for i in range(8):
        turtle.stamp()
        turtle.forward(6)
    turtle.lt(130)
    for i in range(11):
        turtle.stamp()
        turtle.forward(7)
      
def random_triangle_colors(turtle):
    rgb = random.randint(0,255)
    #color =  random.randint(0,255),random.randint(0,255), random.randint(0,255)
    turtle.up()
    turtle.goto(-300,390)
    turtle.down()
    colors = ("red","blue","green")
    theColor = random.choice(colors)
    turtle.color(theColor)
    turtle.rt(80)
    for i in range(11):
        turtle.fillcolor()
        turtle.begin_fill()
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(135)
        turtle.forward(70.7)
        turtle.right(135)
        turtle.forward(50)
        turtle.end_fill()

    turtle.up()
    turtle.goto(-300,-110)
    colors = ("yellow","violet","orange")
    theColor = random.choice(colors)
    turtle.color(theColor)
    turtle.down()
    for i in range(11):
        turtle.fillcolor()
        turtle.begin_fill()
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(135)
        turtle.forward(70.7)
        turtle.right(135)
        turtle.forward(50)
        turtle.end_fill()

    turtle.up()
    turtle.goto(-300,340)
    colors = ("pink","light green","yellow")
    theColor = random.choice(colors)
    turtle.color(theColor)
    turtle.down()
    for i in range(9):
        turtle.fillcolor()
        turtle.begin_fill()
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(135)
        turtle.forward(70.7)
        turtle.left(135)
        turtle.forward(50.7)
        turtle.left(90)
        turtle.end_fill()
    
    turtle.up()
    turtle.goto(200,340)
    colors = ("red","blue","green","light blue","yellow")
    theColor = random.choice(colors)
    turtle.color(theColor)
    turtle.down()
    for i in range(9):
        turtle.fillcolor()
        turtle.begin_fill()
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(135)
        turtle.forward(70.7)
        turtle.left(135)
        turtle.forward(50.7)
        turtle.left(90)
        turtle.end_fill()
main()
