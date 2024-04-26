import turtle

# Set constants for logo dimensions and colors
LOGO_SIZE = 200  # Adjust for desired size
BORDER_WIDTH = 2
CAMERA_RADIUS = 20
DOT_RADIUS = 5
GRADIENT_COLORS = ["#f094fb", "#c964ec", "#843fb5", "#43169c"]

# Initialize the turtle and screen
pen = turtle.Turtle()
screen = turtle.Screen()
screen.setup(LOGO_SIZE, LOGO_SIZE)
screen.tracer(0)  # Turn off animation for smoother drawing

# Create a gradient function for dynamic color selection
def gradient(start_color, end_color, ratio):
    r = int(start_color[1:3], 16) * (1 - ratio) + int(end_color[1:3], 16) * ratio
    g = int(start_color[3:5], 16) * (1 - ratio) + int(end_color[3:5], 16) * ratio
    b = int(start_color[5:], 16) * (1 - ratio) + int(end_color[5:], 16) * ratio
    return f"#{r:02x}{g:02x}{b:02x}"

# Draw the outer square with rounded corners
pen.hideturtle()
pen.penup()
pen.goto(-LOGO_SIZE // 2 + BORDER_WIDTH / 2, LOGO_SIZE // 2 - BORDER_WIDTH / 2)
pen.pendown()
pen.setheading(180)
pen.color(GRADIENT_COLORS[-1])  # Start with the last color in the gradient
pen.width(BORDER_WIDTH)
for _ in range(2):
    pen.circle(LOGO_SIZE // 2 - BORDER_WIDTH / 2, 90)
    pen.color(gradient(GRADIENT_COLORS[-1], GRADIENT_COLORS[0], 0.25))  # Apply gradient
    pen.circle(LOGO_SIZE // 2 - BORDER_WIDTH / 2, 90)
    pen.color(gradient(GRADIENT_COLORS[0], GRADIENT_COLORS[1], 0.25))  # Apply gradient

# Draw the inner circle
pen.penup()
pen.goto(-CAMERA_RADIUS, CAMERA_RADIUS)
pen.pendown()
pen.pensize(0)  # No border for the camera shape
pen.fillcolor(GRADIENT_COLORS[0])  # Use the first color
pen.begin_fill()
pen.circle(CAMERA_RADIUS)
pen.end_fill()

# Draw the camera lens dot
pen.penup()
pen.goto(CAMERA_RADIUS - DOT_RADIUS, CAMERA_RADIUS - DOT_RADIUS)
pen.pendown()
pen.fillcolor("#ffffff")  # White dot
pen.begin_fill()
pen.circle(DOT_RADIUS)
pen.end_fill()

# Display the logo
screen.update()
screen.exitonclick()
