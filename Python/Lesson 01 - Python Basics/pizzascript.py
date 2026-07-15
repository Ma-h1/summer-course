
small = int(input ("What size is the Small Pizza?  "))
smallnumber = int(input("How many Small Pizzas?  "))
smallprice = float(input ("How much are the small Pizzas?  "))
large = int(input ("What size is the Large Pizza?  "))
largenumber = int(input("How many Large Pizzas?"))
largeprice = float(input ("How much are the Large Pizzas?"))
smallx = (3.14 * (small/2) ** 2.0) * smallnumber
largex = (3.14 * (large/2) ** 2.0) * largenumber
print(f"Small is equal to {smallx} square inches of pizza. The cost per square inch is {largex / largeprice:.02f}")
print(f"Large is equal to {largex} square inches of pizza. The cost per square inch is {smallx / smallprice:.02f}")
if smallx > largex:
    print ("Small is better than large.")
elif smallx == largex:
    print ("Small is the same as large.")
else: 
    print ("Large is better than small.")
