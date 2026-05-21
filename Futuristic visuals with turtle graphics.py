import turtle
from turtle import Turtle, Screen
import math
import random
import time

# Setup - Tech aesthetic
screen = Screen()
screen.setup(width=1400, height=900)
screen.bgcolor("#0a0a0a")  # Deep black/charcoal
screen.title("PÄM TECH SYSTEMS - STARK INDUSTRIES PROTOCOL")
screen.tracer(0)
screen.colormode(255)

# TECH COLOR PALETTE (Blue, Black, Ash, Steel)
COLORS = {
    'arc_blue': (0, 150, 255),  # Bright electric blue
    'deep_blue': (0, 80, 200),  # Deep blue
    'steel': (100, 100, 120),  # Steel gray
    'ash': (80, 80, 90),  # Ash gray
    'light_ash': (120, 120, 130),  # Light ash
    'dark_ash': (40, 40, 50),  # Dark ash
    'neon_blue': (0, 200, 255),  # Neon blue glow
    'white_blue': (200, 220, 255),  # White-blue for text
    'black': (10, 10, 15),  # Almost black
    'gold_accent': (255, 200, 50)  # Minimal gold accent
}


# Create turtles for different systems
class TechSystem:
    def __init__(self):
        self.hud_turtle = Turtle()
        self.hud_turtle.speed(0)
        self.hud_turtle.hideturtle()

        self.gear_turtle = Turtle()
        self.gear_turtle.speed(0)
        self.gear_turtle.hideturtle()

        self.data_turtle = Turtle()
        self.data_turtle.speed(0)
        self.data_turtle.hideturtle()

        self.logo_turtle = Turtle()
        self.logo_turtle.speed(0)
        self.logo_turtle.hideturtle()


tech = TechSystem()


def draw_circular_tech_ring(x, y, radius, color, thickness):
    """Draw a high-tech circular ring"""
    ring = Turtle()
    ring.speed(0)
    ring.hideturtle()
    ring.penup()
    ring.goto(x, y - radius)
    ring.pendown()
    ring.color(color)
    ring.pensize(thickness)
    ring.circle(radius)

    # Add dash marks (tech style)
    for angle in range(0, 360, 15):
        ring.penup()
        ring.goto(x, y)
        ring.setheading(angle)
        ring.forward(radius - 5)
        ring.pendown()
        ring.forward(10)
        ring.penup()


def draw_tech_hexagon(x, y, size, color):
    """Draw a hexagon - perfect for tech interfaces"""
    hex_turtle = Turtle()
    hex_turtle.speed(0)
    hex_turtle.hideturtle()
    hex_turtle.penup()
    hex_turtle.goto(x, y)
    hex_turtle.pendown()
    hex_turtle.color(color)
    hex_turtle.pensize(2)

    for _ in range(6):
        hex_turtle.forward(size)
        hex_turtle.right(60)

    # Fill with semi-transparent feel
    hex_turtle.fillcolor(color)

    return hex_turtle


def draw_tech_crosshair(x, y, size, color):
    """Draw a targeting crosshair"""
    cross = Turtle()
    cross.speed(0)
    cross.hideturtle()
    cross.penup()
    cross.goto(x, y - size)
    cross.pendown()
    cross.color(color)
    cross.pensize(2)
    cross.goto(x, y + size)
    cross.penup()
    cross.goto(x - size, y)
    cross.pendown()
    cross.goto(x + size, y)

    # Outer circle
    cross.penup()
    cross.goto(x, y - size)
    cross.pendown()
    cross.circle(size)

    # Corner marks
    for angle in [45, 135, 225, 315]:
        rad = math.radians(angle)
        end_x = x + (size + 10) * math.cos(rad)
        end_y = y + (size + 10) * math.sin(rad)
        cross.penup()
        cross.goto(x, y)
        cross.pendown()
        cross.goto(end_x, end_y)


def draw_tech_circle_array():
    """Draw an array of connected tech circles"""
    positions = [
        (-500, 300), (-400, 280), (-300, 310), (-200, 290),
        (-500, 200), (-400, 180), (-300, 210), (-200, 190),
        (-500, 100), (-400, 80), (-300, 110), (-200, 90)
    ]

    circles = []
    for x, y in positions:
        circle = Turtle()
        circle.speed(0)
        circle.hideturtle()
        circle.penup()
        circle.goto(x, y - 15)
        circle.pendown()
        circle.color(COLORS['neon_blue'])
        circle.pensize(1)
        circle.circle(15)
        circle.dot(5, COLORS['arc_blue'])
        circles.append((circle, x, y))

    # Connect circles with lines
    connector = Turtle()
    connector.speed(0)
    connector.hideturtle()
    connector.color(COLORS['steel'])
    connector.pensize(1)

    for i in range(len(circles) - 1):
        connector.penup()
        connector.goto(circles[i][1], circles[i][2])
        connector.pendown()
        connector.goto(circles[i + 1][1], circles[i + 1][2])


def draw_tech_radar():
    """Draw a rotating radar system"""
    radar = Turtle()
    radar.speed(0)
    radar.hideturtle()

    # Radar rings
    for radius in [40, 80, 120, 160]:
        radar.penup()
        radar.goto(450, -250 - radius)
        radar.pendown()
        radar.color(COLORS['steel'])
        radar.circle(radius)

    # Radar lines
    for angle in [0, 45, 90, 135, 180, 225, 270, 315]:
        rad = math.radians(angle)
        end_x = 450 + 160 * math.cos(rad)
        end_y = -250 + 160 * math.sin(rad)
        radar.penup()
        radar.goto(450, -250)
        radar.pendown()
        radar.goto(end_x, end_y)

    # Center dot
    radar.penup()
    radar.goto(450, -250)
    radar.dot(10, COLORS['arc_blue'])


def draw_tech_gears():
    """Draw rotating gear system (using square and circle shapes)"""
    gears = []

    # Gear 1 - Large
    gear1 = Turtle()
    gear1.speed(0)
    gear1.hideturtle()
    gear1.penup()
    gear1.goto(-500, -250)

    # Gear 2 - Medium
    gear2 = Turtle()
    gear2.speed(0)
    gear2.hideturtle()
    gear2.penup()
    gear2.goto(-400, -200)

    # Gear 3 - Small
    gear3 = Turtle()
    gear3.speed(0)
    gear3.hideturtle()
    gear3.penup()
    gear3.goto(-450, -150)

    for gear, radius, teeth in [(gear1, 60, 12), (gear2, 40, 8), (gear3, 25, 6)]:
        gear.pendown()
        gear.color(COLORS['steel'])
        gear.pensize(2)
        gear.circle(radius)

        # Add teeth (using squares)
        for angle in range(0, 360, 360 // teeth):
            gear.penup()
            gear.setheading(angle)
            gear.forward(radius)
            gear.pendown()
            gear.color(COLORS['arc_blue'])
            gear.begin_fill()
            for _ in range(4):
                gear.forward(8)
                gear.right(90)
            gear.end_fill()
            gear.penup()
            gear.backward(radius)

    return gears


def draw_data_stream():
    """Draw flowing data particles"""
    particles = []
    for i in range(20):
        particle = Turtle()
        particle.speed(0)
        particle.hideturtle()
        particle.shape("circle")
        particle.shapesize(0.3)
        particle.color(COLORS['arc_blue'])
        particle.penup()
        particle.goto(-600 + i * 60, 400)
        particle.showturtle()
        particles.append(particle)
    return particles


def draw_pam_logo_tech():
    """Draw PÄM logo in tech style"""
    logo = Turtle()
    logo.speed(0)
    logo.hideturtle()
    logo.penup()

    # Tech frame around logo
    logo.goto(-250, 320)
    logo.pendown()
    logo.color(COLORS['neon_blue'])
    logo.pensize(3)
    for _ in range(2):
        logo.forward(500)
        logo.right(90)
        logo.forward(60)
        logo.right(90)

    # Main logo text
    logo.penup()
    logo.goto(-180, 360)
    logo.color(COLORS['white_blue'])
    logo.write("PÄM", font=("Arial", 60, "bold"))

    logo.goto(-100, 310)
    logo.color(COLORS['steel'])
    logo.write("TECH SYSTEMS", font=("Arial", 18, "bold"))

    logo.goto(-250, 290)
    logo.color(COLORS['arc_blue'])
    logo.write("STARK-INDUSTRIES PROTOCOL // VER 3.7", font=("Courier", 10, "normal"))


def draw_hud_interface():
    """Draw complete HUD interface"""
    # Left panel
    panel = Turtle()
    panel.speed(0)
    panel.hideturtle()
    panel.penup()

    # Panel border
    panel.goto(-680, -350)
    panel.pendown()
    panel.color(COLORS['steel'])
    panel.pensize(2)
    for _ in range(2):
        panel.forward(150)
        panel.right(90)
        panel.forward(200)
        panel.right(90)

    # System status text
    status_texts = [
        ("SYS_STATUS:", -660, -320),
        ("CORE: ONLINE", -660, -290),
        ("AI: ACTIVE", -660, -260),
        ("WEAPONS: CHARGED", -660, -230),
        ("SHIELD: 98%", -660, -200),
        ("POWER: 100%", -660, -170)
    ]

    for text, x, y in status_texts:
        panel.goto(x, y)
        panel.color(COLORS['arc_blue'])
        panel.write(text, font=("Courier", 11, "bold"))

    # Right panel
    panel.goto(530, -350)
    panel.pendown()
    for _ in range(2):
        panel.forward(150)
        panel.right(90)
        panel.forward(200)
        panel.right(90)

    # Right panel data
    data_texts = [
        ("TARGET:", 550, -320),
        ("ACQUIRED", 550, -290),
        ("DIST: 247m", 550, -260),
        ("LOCK: CONFIRMED", 550, -230),
        ("SYNC: 99.7%", 550, -200)
    ]

    for text, x, y in data_texts:
        panel.goto(x, y)
        panel.color(COLORS['neon_blue'])
        panel.write(text, font=("Courier", 11, "bold"))


def draw_tech_cubes():
    """Draw 3D tech cubes using squares"""
    cube_positions = [
        (550, 250), (600, 200), (500, 150), (580, 100),
        (-550, 200), (-600, 150), (-500, 100), (-580, 50)
    ]

    for x, y in cube_positions:
        cube = Turtle()
        cube.speed(0)
        cube.hideturtle()
        cube.penup()
        cube.goto(x, y)
        cube.pendown()
        cube.color(COLORS['ash'])
        cube.pensize(2)

        # Draw cube (square)
        for _ in range(4):
            cube.forward(30)
            cube.right(90)

        # Draw 3D effect lines
        cube.penup()
        cube.goto(x + 10, y + 10)
        cube.pendown()
        cube.color(COLORS['arc_blue'])
        for _ in range(4):
            cube.forward(30)
            cube.right(90)


def draw_connecting_lines():
    """Draw tech connecting lines across screen"""
    points = [
        (-600, 300), (-400, 350), (-200, 300), (0, 350), (200, 300), (400, 350), (600, 300),
        (-600, 200), (-400, 150), (-200, 200), (0, 150), (200, 200), (400, 150), (600, 200)
    ]

    line_turtle = Turtle()
    line_turtle.speed(0)
    line_turtle.hideturtle()
    line_turtle.color(COLORS['dark_ash'])
    line_turtle.pensize(1)

    for i in range(len(points) - 1):
        line_turtle.penup()
        line_turtle.goto(points[i])
        line_turtle.pendown()
        line_turtle.goto(points[i + 1])


def animate_data_stream(particles):
    """Animate data stream particles"""
    for particle in particles:
        x = particle.xcor()
        y = particle.ycor()
        particle.goto(x + 5, y)
        if x > 600:
            particle.goto(-600, 400)
        particle.color(COLORS['neon_blue'])


def draw_all_shapes_demo():
    """Demonstrate all available shapes in tech style"""
    shapes_turtle = Turtle()
    shapes_turtle.speed(0)
    shapes_turtle.hideturtle()

    # Show all shapes in a tech grid
    shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
    colors = [COLORS['arc_blue'], COLORS['neon_blue'], COLORS['steel'],
              COLORS['ash'], COLORS['light_ash'], COLORS['white_blue']]

    for i, (shape, color) in enumerate(zip(shapes, colors)):
        demo = Turtle()
        demo.shape(shape)
        demo.color(color)
        demo.penup()
        demo.goto(-650 + i * 130, -400)
        demo.shapesize(2)
        demo.stamp()
        demo.hideturtle()

        # Label the shape
        shapes_turtle.goto(-650 + i * 130, -370)
        shapes_turtle.color(COLORS['steel'])
        shapes_turtle.write(shape, font=("Courier", 8, "normal"), align="center")


def busy_tech_animation():
    """Create a busy tech turtle that moves around"""
    tech_turtle = Turtle()
    tech_turtle.speed(0)
    tech_turtle.shape("turtle")
    tech_turtle.color(COLORS['neon_blue'])
    tech_turtle.penup()
    tech_turtle.shapesize(1.5)

    path_points = [
        (-600, 300), (-400, 250), (-200, 350), (0, 280), (200, 320),
        (400, 260), (600, 300), (550, 150), (350, 200), (150, 150),
        (-150, 200), (-350, 150), (-550, 200), (-500, 0), (-300, 50),
        (-100, 0), (100, 50), (300, 0), (500, 50), (450, -100)
    ]

    while True:
        for target in path_points:
            tech_turtle.goto(target)
            tech_turtle.color(random.choice([COLORS['arc_blue'],
                                             COLORS['neon_blue'],
                                             COLORS['white_blue']]))
            tech_turtle.stamp()
            screen.update()
            time.sleep(0.1)


# Main execution
print("🚀 INITIALIZING PÄM TECH SYSTEMS...")
print("⚡ STARK PROTOCOL ACTIVE")
print("🔷 LOADING ALL SHAPES...")

# Draw all tech elements
draw_pam_logo_tech()
draw_hud_interface()
draw_tech_radar()
draw_tech_gears()
draw_tech_circle_array()
draw_tech_cubes()
draw_connecting_lines()
draw_tech_crosshair(0, -200, 80, COLORS['arc_blue'])
draw_tech_crosshair(300, 100, 50, COLORS['steel'])
draw_tech_hexagon(-200, -100, 40, COLORS['neon_blue'])
draw_tech_hexagon(200, -150, 60, COLORS['arc_blue'])
draw_circular_tech_ring(0, -200, 120, COLORS['steel'], 2)
draw_circular_tech_ring(0, -200, 140, COLORS['neon_blue'], 1)
draw_all_shapes_demo()

# Initialize data stream
particles = draw_data_stream()

# Instructions
instruct = Turtle()
instruct.speed(0)
instruct.hideturtle()
instruct.penup()
instruct.goto(-300, -430)
instruct.color(COLORS['steel'])
instruct.write("PÄM TECH // STARK PROTOCOL ACTIVE // CLOSE WINDOW TO EXIT",
               font=("Courier", 10, "normal"))

screen.update()

print("✅ SYSTEMS ONLINE")
print("🔵 ALL SHAPES DEPLOYED")
print("🔄 STARTING BUSY TECH TURTLE...")

# Start animations
try:
    busy_tech_animation()
except:
    pass

# Keep window open
screen.mainloop()