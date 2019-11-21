import turtle
import time
import random

delay = 0.1

#game screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.penup()
food.goto(0,100)

segments = []

#functions
def go_up():
    if head.direction != "down":
        head.direction == "up"

def go_down():
    if head.direction != "up":
        head.direction == "down"

def go_right():
    if head.direction != "left":
        head.direction == "right"

def go_left():
    if head.direction != "right":
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
        head.setx(x - 15)

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")


#game main loop
while True:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()


    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction("stop")
        
            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()

    time.sleep(delay)

wn.mainloop()