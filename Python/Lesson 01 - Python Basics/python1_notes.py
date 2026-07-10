import turtle
import time
import random

WIDTH = 600
HEIGHT = 600
DELAY = 0.1

# Score tracking
score = 0
high_score = 0

# Set up the screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=WIDTH, height=HEIGHT)
window.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, HEIGHT // 2 - 40)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    x = head.xcor()
    y = head.ycor()

    if head.direction == "up":
        head.sety(y + 20)
    if head.direction == "down":
        head.sety(y - 20)
    if head.direction == "left":
        head.setx(x - 20)
    if head.direction == "right":
        head.setx(x + 20)


def reset_game():
    global score, DELAY
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

    score = 0
    DELAY = 0.1
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))


window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")
window.onkey(go_up, "w")
window.onkey(go_down, "s")
window.onkey(go_left, "a")
window.onkey(go_right, "d")

while True:
    window.update()

    if head.xcor() > WIDTH // 2 - 10 or head.xcor() < -WIDTH // 2 + 10 or head.ycor() > HEIGHT // 2 - 10 or head.ycor() < -HEIGHT // 2 + 10:
        reset_game()

    if head.distance(food) < 20:
        x = random.randint(-WIDTH // 2 + 20, WIDTH // 2 - 20)
        y = random.randint(-HEIGHT // 2 + 20, HEIGHT // 2 - 20)
        food.goto(x - (x % 20), y - (y % 20))

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        score += 10
        if score > high_score:
            high_score = score

        DELAY = max(0.05, DELAY - 0.002)
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()
            break

    time.sleep(DELAY)
