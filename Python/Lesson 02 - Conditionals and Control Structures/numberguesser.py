count = 1
secret = int(27)
guess = int(input("Guess an integer number:  "))
while guess != secret:
    if guess > secret:
       print("You are too high!")
    else:
       print("You are too low!")
    if count > 5:
    guess = int(input("Wrong! Guess an integer number:  ")) 
    count += 1

print("Congrats, you got it!")
print(f"It took you {count} times to guess.")