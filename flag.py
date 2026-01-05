import turtle
import time
import random

screen = turtle.Screen()
screen.title("Bangladesh Flag with Moving Clouds")
screen.setup(900, 700)
screen.bgcolor("#87CEEB")

t = turtle.Turtle()
t.speed(6)  # Visible speed

# ground
t.penup()
t.goto(-450, -200)
t.pendown()
t.color("#228B22")
t.begin_fill()
t.forward(900)
t.right(90)
t.forward(200)
t.right(90)
t.forward(900)
t.right(90)
t.forward(200)
t.right(90)
t.end_fill()

# grass
t.color("#006400")
t.pensize(3)
for x in range(-450, 451, 20):
    t.penup()
    t.goto(x, -200)
    t.pendown()
    t.setheading(90)
    t.forward(random.randint(15, 35))

# sun fix: set heading
t.setheading(0)
t.penup()
t.goto(320, 220)
t.pendown()
t.color("#FFD700")
t.begin_fill()
t.circle(40)
t.end_fill()

t.pensize(3)
for i in range(12):
    t.penup()
    t.goto(320, 260)
    t.setheading(i * 30)
    t.forward(50)
    t.pendown()
    t.forward(20)

# pole
t.penup()
t.goto(-100, -250)
t.pendown()
t.color("#8B4513")
t.pensize(10)
t.setheading(90)
t.forward(450)
t.penup()
t.forward(10)
t.dot(20, "gold")

# green part
t.goto(-95, 190)
t.setheading(0)
t.pendown()
t.color("#006A4E")
t.begin_fill()
t.forward(300)
t.right(90)
t.forward(180)
t.right(90)
t.forward(300)
t.right(90)
t.forward(180)
t.right(90)
t.end_fill()

# red circle
t.penup()
t.goto(40, 40)
t.pendown()
t.color("#F42A41")
t.begin_fill()
t.circle(60)
t.end_fill()

t.hideturtle()  # Hide after drawing

# clouds
c1 = turtle.Turtle()
c1.shape("circle")
c1.shapesize(2, 4)
c1.color("white")
c1.penup()
c1.goto(-300, 250)

c2 = turtle.Turtle()
c2.shape("circle")
c2.shapesize(2, 4)
c2.color("white")
c2.penup()
c2.goto(-100, 200)

c3 = turtle.Turtle()
c3.shape("circle")
c3.shapesize(2, 4)
c3.color("white")
c3.penup()
c3.goto(100, 270)

screen.tracer(0)  # No anim for clouds

print("Animation running... Close window to stop.")

while True:
    try:
        # cloud 1
        x = c1.xcor() + 0.5
        y = c1.ycor()
        if x > 500:
            x = -500
            y = random.randint(150, 300)
        c1.goto(x, y)

        # cloud 2
        x = c2.xcor() + 0.3
        y = c2.ycor()
        if x > 500:
            x = -500
            y = random.randint(150, 300)
        c2.goto(x, y)

        # cloud 3
        x = c3.xcor() + 0.6
        y = c3.ycor()
        if x > 500:
            x = -500
            y = random.randint(150, 300)
        c3.goto(x, y)

        screen.update()
        time.sleep(0.01)
    except:
        break