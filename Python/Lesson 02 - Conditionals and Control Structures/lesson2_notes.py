number = int(input("Please enter a number:  "))
if number == 0:
    print("Zero")
elif number >= 1:
    print("Positive")
    if number % 2 == 0:
        print("Also, the number is even, even though you didn't ask.")
    else:
        print("Also, the number is odd, even though you didn't ask.")
else:
    print("Negative")


age = int(input("Please enter your age:  "))
if age < 0:
    print("You can't have a negative age, dummy.")
elif age < 13:
    print("Child")
elif age <=19:
    print ("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")


num1 = int(input("Please enter a number:  "))
num2 = int(input("Please enter a second number:  "))
if num1 == num2:
    print("The numbers are equal.")
elif num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")

grade = float(input("Please enter your grade:  "))
if grade >= 90:
    print("A!")
elif grade >= 80:
    print("B!")
elif grade >= 70:
    print("C but without an exclaimation point because that's not really great")
elif grade >= 60:
    print("D... this isn't passing in most states.")
else:
    print("F. You suck.")

userinput = input("Please enter a string:  ")
if len(userinput) >= 10:
    print("Long String!")
else:
    print("Short String")

numberinput = int(input("Please enter a number:  "))
if numberinput >= 10 and numberinput <= 20:
    print("Number is in range.")
else:
    print("Number is out of range.")

letterinput = input("Please enter a letter:  ")
if len(letterinput) > 1:
    print("Please enter only one letter.")

elif letterinput == "a" or letterinput == "e" or letterinput == "i" or letterinput == "o" or letterinput == "u":
    print("Vowel")
else:
    print ("Consonant")

year = int(input("Please enter a year:  "))
if year % 4 == 0 and year % 100 != 0:
    print("Leap Year!")
elif year % 400 == 0:
    print ("Leap Year!")
else:
    print("Not a Leap Year.")
    
colors = ["red", "white", "blue"]
for color in colors:
    print(color)

for number in range(20,51,2)
print(number)


number = int(input("Please enter an even number:  "))
while number % 2 != 0:
    print("This is an odd number.")
    number = int(input("Please enter an even number:  "))

count = 1
secret = int(27)
guess = int(input("Guess an integer number:  "))
while guess != secret:
    if guess > secret:
       print("You are too high!")
    else:
       print("You are too low!")
    if count > 5

    guess = int(input("Wrong! Guess an integer number:  ")) 
    count += 1

print("Congrats, you got it!")
print(f"It took you {count} times to guess.")