import random
num = random.randrange(1,101)
print(f"The number is {num}")
if num < 50:
    print("Number is less than 50.")
elif num > 50:
    print("Number is more than 50.")
else:
    print("The number is 50.")