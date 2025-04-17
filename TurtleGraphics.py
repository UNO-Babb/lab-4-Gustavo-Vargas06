#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle
screen = turtle.Screen
kev = turtle.Turtle()
def drawSquare(kev, size):
    for i in range(4):
        kev.forward(size)
        kev.right(90)
        
#drawSquare(kev, 50)

def drawPoly(kev, size, sides): 
    for  s in range(sides):
        kev.forward(size)
        kev.right(360/sides)
        
#drawPoly(kev, 50, 5)
#drawPoly(kev, 50, 8)

def fillCorner(kev, corner):
    drawSquare(kev, 100)
    if corner == 1:
        kev.begin_fill()
        drawSquare(kev, 50)
        kev.end_fill()
    elif corner == 2:
        kev.forward(50)
        kev.begin_fill()
        drawSquare(kev, 50)
        kev.end_fill()
    elif corner == 3:
        kev.right(90)
        kev.forward(50)
        kev.left(90)
        kev.begin_fill()
        drawSquare(kev, 50)
        kev.end_fill()
    elif corner == 4:
        kev.right(90)
        kev.forward(50)
        kev.left(90)
        kev.forward(50)
        kev.begin_fill()
        drawSquare(kev, 50)
        kev.end_fill()
    
#fillCorner(kev, 2)
#fillCorner(kev, 3)

def squaresInsquares(kev, num, size):
    kev.up()
    kev.left(180)
    kev.forward(size * num)
    kev.down()
    kev.right(90)
    kev.forward(size * num)
    kev.right(90)
    while num > 0:
       drawSquare(kev, (size * num) * 2)
       kev.up()
       kev.right(90)
       kev.forward(size)
       kev.left(90)
       kev.forward(size)
       kev.down()
       num = num - 1

#squaresInsquares(kev, 5, 25)
#squaresInsquares(kev, 3, 25)
squaresInsquares(kev, 10, 25)


main()
