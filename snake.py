import turtle
import time

delay = 0.1

#game screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "right"

#functions
def up():
    head.direction == "up"

def down():
    head.direction == "down"

def right():
    head.direction == "right"

def left():
    head.direction == "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 15)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 15)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 15)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x + 15)

#keyboard bindings
window.listen()

#game main loop
while True:
    window.update()

    move()

    time.sleep(delay)

window.mainloop()