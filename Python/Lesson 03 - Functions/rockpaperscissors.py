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