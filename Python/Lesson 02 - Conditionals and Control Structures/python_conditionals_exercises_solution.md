# Hands-On: Python Conditional Statements - Solutions

These exercises focus on using `if`, `elif`, and `else` statements to control program flow. You'll work with comparison operators, logical operators, and data types from Lesson 1 to make decisions in your code.

---

### Exercise 1: Check if a Number is Positive

**Goal**: Write a program that checks if a number is positive using an `if` statement.

```python
number = 15

if number > 0:
    print("The number is positive")
```

✅ *Check*: Should print "The number is positive" if the number is greater than 0.

---

### Exercise 2: Even or Odd

**Goal**: Check if a number is even or odd using `if` and `else`.

```python
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

✅ *Check*: Should print "Even" or "Odd" based on the number.

---

### Exercise 3: Age Category

**Goal**: Use `if`, `elif`, and `else` to categorize a person by age.

```python
age = 25

if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")
```

✅ *Check*: Should print the correct category based on age.

---

### Exercise 4: Compare Two Numbers

**Goal**: Compare two numbers and print which is larger, or if they're equal.

```python
a = 10
b = 20

if a > b:
    print("a is larger")
elif b > a:
    print("b is larger")
else:
    print("a and b are equal")
```

✅ *Check*: Should print "a is larger", "b is larger", or "a and b are equal".

---

### Exercise 5: Grade Converter

**Goal**: Convert a numeric grade to a letter grade.

```python
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

✅ *Check*: Should print the correct letter grade.

---

### Exercise 6: String Length Check

**Goal**: Check if a string has more than 10 characters.

```python
text = "Hello, Python!"

if len(text) > 10:
    print("Long string")
else:
    print("Short string")
```

✅ *Check*: Should print "Long string" if length > 10, else "Short string".

---

### Exercise 7: Logical AND Operator

**Goal**: Check if a number is between 10 and 20 (inclusive) using the `and` operator.

```python
number = 15

if number >= 10 and number <= 20:
    print("Number is in range")
else:
    print("Out of range")
```

✅ *Check*: Should print "Number is in range" if between 10 and 20, else "Out of range".

---

### Exercise 8: Logical OR Operator

**Goal**: Check if a character is a vowel using the `or` operator.

```python
letter = "e"

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("Vowel")
else:
    print("Consonant")

# Alternative solution using 'in'
if letter in "aeiou":
    print("Vowel")
else:
    print("Consonant")
```

✅ *Check*: Should print "Vowel" if the letter is a, e, i, o, or u, else "Consonant".

---

### Exercise 9: Password Validator

**Goal**: Check if a password meets basic requirements (at least 8 characters AND contains a number).

```python
password = "secure123"

has_number = any(char.isdigit() for char in password)

if len(password) >= 8 and has_number:
    print("Valid password")
else:
    print("Invalid password")

# Beginner-friendly alternative
contains_digit = False
for char in password:
    if char.isdigit():
        contains_digit = True
        break

if len(password) >= 8 and contains_digit:
    print("Valid password")
else:
    print("Invalid password")
```

✅ *Check*: Should print "Valid password" or "Invalid password".

---

### Exercise 10: Leap Year Checker

**Goal**: Determine if a year is a leap year.

```python
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
```

✅ *Check*: Should print "Leap year" or "Not a leap year".

---

### Exercise 11: List Membership

**Goal**: Check if a fruit is in a list of available fruits.

```python
available_fruits = ["apple", "banana", "orange", "mango"]
fruit = "banana"

if fruit in available_fruits:
    print("In stock")
else:
    print("Out of stock")
```

✅ *Check*: Should print "In stock" if fruit is in the list, else "Out of stock".

---

### Exercise 12: Temperature Advisory

**Goal**: Give weather advice based on temperature.

```python
temperature = 22

if temperature < 0:
    print("Freezing! Stay inside.")
elif temperature <= 15:
    print("Cold. Wear a jacket.")
elif temperature <= 25:
    print("Pleasant weather.")
else:
    print("Hot! Stay hydrated.")
```

✅ *Check*: Should print appropriate advice based on temperature.

---

### Exercise 13: Discount Calculator

**Goal**: Calculate a discount based on purchase amount.

```python
purchase_amount = 75

if purchase_amount >= 100:
    discount = 0.20
elif purchase_amount >= 50:
    discount = 0.10
else:
    discount = 0

final_price = purchase_amount * (1 - discount)
print(f"Discount: {discount * 100}%")
print(f"Final price: ${final_price:.2f}")
```

✅ *Check*: Should print the discount percentage and final price.

---

### Exercise 14: Dictionary Key Check

**Goal**: Check if a key exists in a dictionary and print its value.

```python
student = {"name": "Alice", "age": 20, "major": "Computer Science"}
key = "age"

if key in student:
    print(student[key])
else:
    print("Key not found")
```

✅ *Check*: Should print the value if key exists, else "Key not found".

---

### Exercise 15: Nested Conditionals - BMI Calculator

**Goal**: Calculate BMI category using nested `if` statements.

```python
weight = 70  # kg
height = 1.75  # meters

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"BMI: {bmi:.1f} - Underweight")
elif bmi < 25:
    print(f"BMI: {bmi:.1f} - Normal weight")
elif bmi < 30:
    print(f"BMI: {bmi:.1f} - Overweight")
else:
    print(f"BMI: {bmi:.1f} - Obese")
```

✅ *Check*: Should calculate BMI and print the correct category.

---

### Exercise 16: Type Checking

**Goal**: Check the data type of a variable and print different messages for different types.

```python
value = 42

if type(value) == int:
    print("This is an integer")
elif type(value) == float:
    print("This is a float")
elif type(value) == str:
    print("This is a string")
elif type(value) == list:
    print("This is a list")
else:
    print("This is another type")

# Alternative using isinstance()
if isinstance(value, int):
    print("This is an integer")
elif isinstance(value, float):
    print("This is a float")
elif isinstance(value, str):
    print("This is a string")
elif isinstance(value, list):
    print("This is a list")
else:
    print("This is another type")
```

✅ *Check*: Should identify if value is an int, float, str, list, or other type.

---

### Exercise 17: Multiple Conditions with NOT

**Goal**: Check if a number is NOT in a specific range (10-20).

```python
number = 25

if not (number >= 10 and number <= 20):
    print("Outside range")
else:
    print("In range")

# Alternative
if number < 10 or number > 20:
    print("Outside range")
else:
    print("In range")
```

✅ *Check*: Should print "Outside range" if not between 10 and 20, else "In range".

---

### Exercise 18: Login System

**Goal**: Create a simple login checker that validates username AND password.

```python
correct_username = "admin"
correct_password = "pass123"
entered_username = "admin"
entered_password = "pass123"

if entered_username == correct_username and entered_password == correct_password:
    print("Login successful")
else:
    print("Login failed")
```

✅ *Check*: Should print "Login successful" or "Login failed".

---

### Exercise 19: Triangle Type Classifier

**Goal**: Classify a triangle based on side lengths.

```python
side1 = 5
side2 = 5
side3 = 8

if side1 == side2 == side3:
    print("Equilateral")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles")
else:
    print("Scalene")
```

✅ *Check*: Should print the correct triangle type.

---

### Exercise 20: Complex Eligibility Check

**Goal**: Check if someone is eligible for a senior discount.

```python
age = 62
is_member = True

if age >= 65 or (age >= 60 and is_member):
    print("Eligible for discount")
else:
    print("Not eligible")
```

✅ *Check*: Should print "Eligible for discount" or "Not eligible".
