import random
import time
count = 1
numlist = range(1,101)
secret = random.choice(numlist)
userguess = int(input("I have chosen a secret number between 1 and 100.  If you guess it, you'll get a prize!:  "))
while userguess != secret:
    if userguess > secret:
        print("Too High!")
    else:
        print("Too Low")
    userguess = int(input("Please guess a number between 1 and 100:  "))
    count += 1
print(f"You did it, the secret number was {secret} and it took you {count} tries.")
import turtle
time.sleep(3)
pen = turtle.Turtle()
def curve():
   for i in range(200):
       pen.right(1)
       pen.forward(1)

def heart():
   pen.fillcolor('red')
   pen.begin_fill()
   pen.left(140)
   pen.forward(113)
   curve()
   pen.left(120)
   curve()
   pen.forward(112)
   pen.end_fill()

def txt():
   pen.up()
   pen.setpos(-68, 95)
   pen.down()
   pen.color('lightgreen')
   pen.write("I Love Diana!", font=("Verdana", 12, "bold"))
heart()
txt()
pen.hideturtle()
turtle.done()