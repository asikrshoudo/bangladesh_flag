import turtle
import time
import random

# --- 1. Screen Setup ---
screen = turtle.Screen()
screen.title("Bangladesh Flag with Moving Clouds")
screen.setup(width=900, height=700)
screen.bgcolor("#87CEEB")  # Sky Blue
screen.tracer(0)  # Turn off auto-update for smooth animation

# --- 2. Flag & Scene Constants ---
# Flag Ratio 10:6
FLAG_WIDTH = 300
FLAG_HEIGHT = 180
FLAG_RADIUS = FLAG_WIDTH * 0.2  # Radius is 20% of width
POLE_HEIGHT = 450

# --- 3. Drawing Functions ---

def draw_rectangle(t, color, width, height):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

def draw_circle(t, color, r):
    t.color(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def draw_ground():
    g = turtle.Turtle()
    g.hideturtle()
    g.speed(0)
    
    # Soil/Ground Base
    g.penup()
    g.goto(-450, -200)
    g.pendown()
    draw_rectangle(g, "#228B22", 900, 200) # Forest Green
    
    # Grass Effect
    g.color("#006400") # Dark Green
    g.pensize(3)
    g.setheading(90)
    for x in range(-450, 450, 20):
        g.penup()
        g.goto(x, -200)
        g.pendown()
        # Random grass height
        g.forward(random.randint(15, 35))

def draw_sun():
    s = turtle.Turtle()
    s.hideturtle()
    s.penup()
    s.goto(320, 220)
    s.pendown()
    s.color("#FFD700") # Gold
    s.begin_fill()
    s.circle(40)
    s.end_fill()
    
    # Sun Rays
    s.pensize(3)
    for i in range(12):
        s.penup()
        s.goto(320, 260) # Center of sun
        s.setheading(i * 30)
        s.forward(50)
        s.pendown()
        s.forward(20)

def draw_flag_and_pole():
    p = turtle.Turtle()
    p.speed(0)
    p.hideturtle()
    
    # 1. The Pole
    p.penup()
    p.goto(-100, -250)
    p.color("#8B4513") # Saddle Brown
    p.pensize(10)
    p.setheading(90) # Upwards
    p.pendown()
    p.forward(POLE_HEIGHT)
    
    # Pole Top Knob
    p.color("gold")
    p.dot(20)
    
    # 2. Green Field (Starting from top of pole)
    start_x = -95 # Just beside the pole
    start_y = -250 + POLE_HEIGHT - 10 # Little bit down from top
    
    p.penup()
    p.goto(start_x, start_y)
    p.setheading(0) # Face right
    draw_rectangle(p, "#006A4E", FLAG_WIDTH, FLAG_HEIGHT) # Official Bottle Green
    
    # 3. Red Disc
    # Center logic: 9/20 of width from left (45% of width)
    center_x = start_x + (FLAG_WIDTH * 0.45)
    # Vertical center: Half of height
    center_y_pos = start_y - (FLAG_HEIGHT / 2)
    
    # Move to start drawing circle (turtle draws from bottom edge of circle)
    p.penup()
    p.goto(center_x, center_y_pos - FLAG_RADIUS)
    draw_circle(p, "#F42A41", FLAG_RADIUS) # Official Red

# --- 4. Cloud Class for Animation ---
class Cloud:
    def __init__(self, x, y, speed):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.t.color("white")
        self.t.speed(0)
        self.x = x
        self.y = y
        self.speed = speed
        self.draw_shape() # Draw cloud once inside the turtle shape
        
    def draw_shape(self):
        # We define the cloud shape using a custom polygon or stamps
        # To make it movable easily, we will just use the turtle as a drawing cursor
        # but re-drawing creates lag. Better approach: Use turtle 'shape'
        self.t.shape("circle")
        self.t.shapesize(stretch_wid=2, stretch_len=4) # Oval shape cloud
    
    def move(self):
        self.x += self.speed
        if self.x > 500: # Reset if goes off screen
            self.x = -500
            self.y = random.randint(150, 300)
        self.t.goto(self.x, self.y)
        self.t.showturtle()

# --- 5. Main Execution ---

# Draw Static Elements
draw_ground()
draw_sun()
draw_flag_and_pole()

# Create Clouds
clouds = [
    Cloud(-300, 250, 0.5),
    Cloud(-100, 200, 0.3),
    Cloud(100, 270, 0.6)
]

# --- 6. Animation Loop ---
print("Animation Started... Press Close Button to Exit.")
while True:
    try:
        for cloud in clouds:
            cloud.move()
        
        screen.update() # Update the screen manually
        time.sleep(0.01) # Small delay to control framerate
        
    except turtle.Terminator:
        break # Exit cleanly if window is closed
