# Hands-On: Python Conditional Statements

These exercises focus on using `if`, `elif`, and `else` statements to control program flow. You'll work with comparison operators, logical operators, and data types from Lesson 1 to make decisions in your code.

---

### Exercise 1: Check if a Number is Positive

**Goal**: Write a program that checks if a number is positive using an `if` statement.

```python
number = 15
```

✅ *Check*: Should print "The number is positive" if the number is greater than 0.

---

### Exercise 2: Even or Odd

**Goal**: Check if a number is even or odd using `if` and `else`.

```python
number = 7
```

✅ *Check*: Should print "Even" or "Odd" based on the number.

---

### Exercise 3: Age Category

**Goal**: Use `if`, `elif`, and `else` to categorize a person by age.

- Under 13: "Child"
- 13-19: "Teenager"
- 20-64: "Adult"
- 65+: "Senior"

```python
age = 25
```

✅ *Check*: Should print the correct category based on age.

---

### Exercise 4: Compare Two Numbers

**Goal**: Compare two numbers and print which is larger, or if they're equal.

```python
a = 10
b = 20
```

✅ *Check*: Should print "a is larger", "b is larger", or "a and b are equal".

---

### Exercise 5: Grade Converter

**Goal**: Convert a numeric grade to a letter grade.

- 90+: A
- 80-89: B
- 70-79: C
- 60-69: D
- Below 60: F

```python
score = 85
```

✅ *Check*: Should print the correct letter grade.

---

### Exercise 6: String Length Check

**Goal**: Check if a string has more than 10 characters.

```python
text = "Hello, Python!"
```

✅ *Check*: Should print "Long string" if length > 10, else "Short string".

---

### Exercise 7: Logical AND Operator

**Goal**: Check if a number is between 10 and 20 (inclusive) using the `and` operator.

```python
number = 15
```

✅ *Check*: Should print "Number is in range" if between 10 and 20, else "Out of range".

---

### Exercise 8: Logical OR Operator

**Goal**: Check if a character is a vowel using the `or` operator.

```python
letter = "e"
```

✅ *Check*: Should print "Vowel" if the letter is a, e, i, o, or u, else "Consonant".

---

### Exercise 9: Password Validator

**Goal**: Check if a password meets basic requirements (at least 8 characters AND contains a number).

```python
password = "secure123"
```

✅ *Check*: Should print "Valid password" or "Invalid password".

---

### Exercise 10: Leap Year Checker

**Goal**: Determine if a year is a leap year.

Rules:
- Divisible by 4 AND not divisible by 100, OR
- Divisible by 400

```python
year = 2024
```

✅ *Check*: Should print "Leap year" or "Not a leap year".

---

### Exercise 11: List Membership

**Goal**: Check if a fruit is in a list of available fruits.

```python
available_fruits = ["apple", "banana", "orange", "mango"]
fruit = "banana"
```

✅ *Check*: Should print "In stock" if fruit is in the list, else "Out of stock".

---

### Exercise 12: Temperature Advisory

**Goal**: Give weather advice based on temperature.

- Below 0: "Freezing! Stay inside."
- 0-15: "Cold. Wear a jacket."
- 16-25: "Pleasant weather."
- Above 25: "Hot! Stay hydrated."

```python
temperature = 22
```

✅ *Check*: Should print appropriate advice based on temperature.

---

### Exercise 13: Discount Calculator

**Goal**: Calculate a discount based on purchase amount.

- $100+: 20% discount
- $50-$99: 10% discount
- Under $50: No discount

```python
purchase_amount = 75
```

✅ *Check*: Should print the discount percentage and final price.

---

### Exercise 14: Dictionary Key Check

**Goal**: Check if a key exists in a dictionary and print its value.

```python
student = {"name": "Alice", "age": 20, "major": "Computer Science"}
key = "age"
```

✅ *Check*: Should print the value if key exists, else "Key not found".

---

### Exercise 15: Nested Conditionals - BMI Calculator

**Goal**: Calculate BMI category using nested `if` statements.

- BMI < 18.5: "Underweight"
- BMI 18.5-24.9: "Normal weight"
- BMI 25-29.9: "Overweight"
- BMI 30+: "Obese"

Formula: BMI = weight (kg) / height (m)²

```python
weight = 70  # kg
height = 1.75  # meters
```

✅ *Check*: Should calculate BMI and print the correct category.

---

### Exercise 16: Type Checking

**Goal**: Check the data type of a variable and print different messages for different types.

```python
value = 42
```

✅ *Check*: Should identify if value is an int, float, str, list, or other type.

---

### Exercise 17: Multiple Conditions with NOT

**Goal**: Check if a number is NOT in a specific range (10-20).

```python
number = 25
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
```

✅ *Check*: Should print "Login successful" or "Login failed".

---

### Exercise 19: Triangle Type Classifier

**Goal**: Classify a triangle based on side lengths.

- All sides equal: "Equilateral"
- Two sides equal: "Isosceles"
- All sides different: "Scalene"

```python
side1 = 5
side2 = 5
side3 = 8
```

✅ *Check*: Should print the correct triangle type.

---

### Exercise 20: Complex Eligibility Check

**Goal**: Check if someone is eligible for a senior discount.

Requirements:
- Age 65+ OR
- Age 60+ AND member is True

```python
age = 62
is_member = True
```

✅ *Check*: Should print "Eligible for discount" or "Not eligible".
