for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


import random
rps_list = ["rock", "paper", "scissors"]
computerchoice = random.choice(rps_list)
userinput = input("Select rock, paper, or scissors:  ")
if userinput not in rps_list:
    print("Please only type rock, paper, or scissors.")
print(f"Computer selects {computerchoice}")
if computerchoice == userinput:
    print("Tie!")
elif computerchoice == "rock" and userinput == "paper":
    print("You win")
elif computerchoice == "paper" and userinput == "scissors" :
    print("You win")
elif computerchoice == "scissors" and userinput == "rock":
    print("You win")
else:
    print("You lose")
        
import random
count = 1
numlist = range(1,101)
secret = random.choice(numlist)
userguess = int(input("Please guess a number between 1 and 100:  "))
while userguess != secret:
    if userguess > secret:
        print("Too High!")
    else:
        print("Too Low")
    userguess = int(input("Please guess a number between 1 and 100:  "))
    count += 1
print(f"You did it, the secret number was {secret} and it took you {count} tries.")
