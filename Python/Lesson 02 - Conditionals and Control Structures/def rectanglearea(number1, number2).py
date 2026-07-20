


def tip(tot:  float, perc:  float):
    result = tot * (perc/100)
    return result
total = float(input("What is the total of the meal?  "))
percent = float(input("What percent would you like to tip?  "))

result = tip(total, percent)

subtotal = result + total
print(f"The tip amount is {result:.02f}")
print(f"The total of the meal with tip is {subtotal:.02f}.")