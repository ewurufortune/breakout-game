import turtle


# Set up the game window
wn = turtle.Screen()
wn.title("Breakout Clone")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Bricks
bricks = []

brick_width = 80
brick_height = 20

for i in range(5):
    for j in range(8):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.shapesize(stretch_wid=brick_height / 20, stretch_len=brick_width / 20)
        brick.color("red")
        brick.penup()
        brick.goto(-350 + j * 100, 250 - i * 25)
        bricks.append(brick)

# Paddle movement
def paddle_right():
    x = paddle.xcor()
    x += 50
    if x > 350:
        x = 350
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x -= 50
    if x < -350:
        x = -350
    paddle.setx(x)

# Keyboard bindings
wn.listen()
wn.onkey(paddle_right, "Right")
wn.onkey(paddle_left, "Left")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Paddle and ball collisions
    if (ball.ycor() > -240) and (ball.ycor() < -230) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.sety(-230)
        ball.dy *= -1

    # Brick and ball collisions
    for brick in bricks:
        if brick.distance(ball) < 20:
            brick.hideturtle()
            bricks.remove(brick)
            ball.dy *= -1

    # Check for game over
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Check for victory
    if not bricks:
        wn.title("You Win!")
        break

wn.mainloop()