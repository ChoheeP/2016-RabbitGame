import turtle
import random
import math
import time

#Set up screen
screen = turtle.Screen()
screen.bgpic("background.gif")
screen.setup(600, 600)
screen.tracer(1)

#Draw line
line = turtle.Turtle()
line.hideturtle()
line.speed(0)
line.penup()
line.setposition(-300, -300)
line.pendown()
line.pensize(2)
for i in range(4):
    line.forward(600)
    line.left(90)

#Create rabbit turtle
rabbit = turtle.Turtle()
screen.addshape("rabbit.gif")
rabbit.shape("rabbit.gif")
rabbit.speed(0)
rabbit.penup()
rabbit.setposition(0, -250)

#creat the score variable
score = 0
playing = False

#Create carrot turtle
carrot = turtle.Turtle()
screen.addshape("carrot.gif")
carrot.shape("carrot.gif")
carrot.speed(0)
carrot.penup()
carrot.setposition(random.randint(-280, 280), 300)
carrot.right(90)

#define function
def turnleft():
    if rabbit.heading() == 0:
        rabbit.left(180)

def turnright():
    if rabbit.heading() == 180:
        rabbit.right(180)

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 50:
        return True
    else:
        return False

def start():
  global playing
  if playing==False:
    playing=True
    turtle.clear()
    play()

if playing:
    turtle.sleep(2)

def message(m1,m2):
    turtle.clear()
    turtle.goto(0,90)
    turtle.color("hot pink")
    turtle.write(m1, False, 'center', ('', 50))
    turtle.goto(0, -90)
    turtle.write(m2, False, 'center', ('', 45))
    turtle.home()

#set keyboard
turtle.title("Eating Bunny")
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkeypress(start,"space")
turtle.penup()
message("Eating Bunny","[space]")
turtle.hideturtle()
time.sleep(1)

def play():
    global score
    global playing

while True:
    rabbit.forward(score+2)

    # rabbit boundary
    if rabbit.xcor() >= 280:
        rabbit.left(180)
    if rabbit.xcor() <= -280:
        rabbit.right(180)

    # move the carrot
    carrot.forward(score+1)

    # collision checking
    if isCollision(rabbit, carrot):
        carrot.setposition(random.randint(-280, 280), 300)
        score += 1

        # draw the score on the screen
        line.undo()
        line.penup()
        line.hideturtle()
        line.setposition(-280, 270)
        scorestring = "Score = %s" % score
        line.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

    elif carrot.ycor() < -300:
        carrot.hideturtle()
        text = 'Score: ' + str(score)
        message('Game Over', text)
        playing = False
        break

screen.mainloop()