import turtle
import random
import time
# Function to play sound
def play_sound():
    try:
        playsound("celebration.mp3", block=False)  # Replace with your sound file
    except:
        print("Sound file not found! Add 'celebration.mp3' to the same directory.")

# Function to draw colorful fireworks
def draw_firework(t, size, color):
    t.color(color)
    for _ in range(36):
        t.forward(size)
        t.right(170)

# Function to animate fireworks
def fireworks(x=None, y=None):
    firework_turtle = turtle.Turtle()
    firework_turtle.speed(0)
    firework_turtle.hideturtle()
    colors = ["red", "yellow", "blue", "green", "magenta", "cyan", "orange", "white"]

    for _ in range(6):
        firework_turtle.penup()
        firework_turtle.goto(random.randint(-300, 300), random.randint(-200, 200))
        firework_turtle.pendown()
        draw_firework(firework_turtle, random.randint(50, 150), random.choice(colors))
        time.sleep(0.3)  # Short delay for animation

# Function to animate floating balloons
def balloons():
    balloon_turtles = []
    colors = ["red", "blue", "green", "yellow", "pink", "purple", "orange"]
    for _ in range(10):  # Create multiple balloons
        t = turtle.Turtle()
        t.shape("circle")
        t.shapesize(random.uniform(1, 2))  # Random balloon size
        t.color(random.choice(colors))
        t.penup()
        t.goto(random.randint(-300, 300), -300)  # Start from bottom
        t.speed(random.randint(1, 3))
        balloon_turtles.append(t)

    for _ in range(200):  # Animate balloons upwards
        for t in balloon_turtles:
            t.sety(t.ycor() + random.randint(2, 6))
            if t.ycor() > 300:  # Reset balloon position
                t.goto(random.randint(-300, 300), -300)
        time.sleep(0.05)

# Function to create twinkling stars
def twinkling_stars():
    star_turtle = turtle.Turtle()
    star_turtle.hideturtle()
    star_turtle.penup()
    star_turtle.color("white")

    for _ in range(30):  # Draw multiple stars
        x = random.randint(-350, 350)
        y = random.randint(-250, 250)
        star_turtle.goto(x, y)
        star_turtle.dot(random.randint(2, 6))  # Small twinkling dots

# Function to display the New Year message
def display_message():
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.color("gold")
    writer.penup()
    writer.goto(0, 0)
    writer.write("🎆 Happy New Year 2025 🎆", align="center", font=("Arial", 32, "bold"))
    writer.goto(0, -50)
    writer.write("May this year bring you joy, success, and dreams come true! 🌟", align="center", font=("Arial", 16, "italic"))

# Function to display everything together
def main():
    # Play sound
    play_sound()

    # Setup screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Happy New Year Celebration 🌟✨")

    # Show twinkling stars
    twinkling_stars()

    # Start balloon animation in the background
    turtle.ontimer(balloons, t=500)  # Delay to start balloons

    # Fireworks animation on click
    screen.onclick(fireworks)

    # Display message on "Enter" key
    screen.listen()
    screen.onkey(display_message, "Return")  # Press 'Enter' to display message

    screen.mainloop()

# Run the program
if __name__ == "__main__":
    main()
