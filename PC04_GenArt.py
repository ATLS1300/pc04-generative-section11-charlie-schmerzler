"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: YOUR NAME HERE

********* HEY, READ THIS FIRST **********

This is a description of the code that is written out below. This script is start code for PC04 + beyond. 
It imports random and math libraries along with the turtle libraries.
You should add your name(s), to line 4, and replace this description with one that describes what your code does!
(Hint: what patterns does it make? should it evoke any emotions?

"""
import turtle
import math, random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)
colorPalette = [(255,0,0), (255,128,0), (255,255,0), (128,255,0), (0,255,0),
                (0,255,128), (0,255,255), (0,128,255), (0,0,255), (127,0,255),
                (255,0,255), (255,0,127)]
# Create a panel to draw on. 
panel = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
panel.bgcolor("Black")
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.speed(0)
t2.speed(0)


for i in range(30):
    for a in range(2):
        t1.goto(random.randint(-300,300),random.randint(-300,300))
        t1.down()
        t1.color(random.choice(colorPalette))
        t1.begin_fill()
        t1.circle(random.randint(20,60))
        t1.end_fill()
        t1.up()
    for b in range(2):
        t2.goto(random.randint(-300,300), random.randint(-300,300))
        t2.down()
        t2.color(random.choice(colorPalette))
        x = random.randint(50,150)
        t2.begin_fill()
        for c in range(4):
            t2.forward(x)
            t2.right(90)
        t2.end_fill()
        t2.up()
t1.done()
t2.done()

        




# panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
# turtle.done()
