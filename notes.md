# Python Mastery – Day 0 🚀

## Quick Revision of Python Fundamentals

---

# 🖨 Print Statement

```python
print("Hello World")
```

### Output

```python
Hello World
```

### Purpose

Used to display output on the screen.

---

# 📦 Variables & Data Types

```python
name = "Ankit"
age = 20
height = 5.8
is_student = True
```

| Data Type | Example   |
| --------- | --------- |
| String    | `"Ankit"` |
| Integer   | `20`      |
| Float     | `5.8`     |
| Boolean   | `True`    |

### Purpose

Variables are used to store data.

---

# ⌨ User Input

```python
name = input("Enter your name: ")

print("Welcome", name)
```

### Purpose

Used to take input from the user.

---

# ➕ Arithmetic Operators

```python
x = 10
y = 3
```

| Operator | Meaning        | Example  |
| -------- | -------------- | -------- |
| +        | Addition       | `x + y`  |
| -        | Subtraction    | `x - y`  |
| *        | Multiplication | `x * y`  |
| /        | Division       | `x / y`  |
| //       | Floor Division | `x // y` |
| %        | Modulus        | `x % y`  |
| **       | Power          | `x ** y` |

---

# 🔀 Conditional Statements

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

### Purpose

Used for decision making.

---

# 🔁 While Loop

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

### Purpose

Repeats code while condition is True.

---

# 🔄 For Loop

```python
games = ["Minecraft", "Valorant", "GTA"]

for game in games:
    print(game)
```

### Purpose

Used to iterate through items.

---

# 📋 Lists

```python
games = ["Minecraft", "Valorant", "GTA"]

print(games[0])

games.append("BGMI")

print(games)
```

### Output

```python
['Minecraft', 'Valorant', 'GTA', 'BGMI']
```

### Purpose

Stores multiple values in one variable.

---

# ⚙ Functions

```python
def greet(name):
    print("Hello", name)

greet("Ankit")
```

### Purpose

Reusable block of code.

---

# ↩ Return Statement

```python
def multiply(a, b):
    return a * b

result = multiply(5, 10)

print(result)
```

### Output

```python
50
```

### Purpose

Returns value from a function.

---

# 🎮 Mini Project – Number Guessing Game

```python
import random

secret = random.randint(1, 10)

guess = int(input("Guess the number: "))

if guess == secret:
    print("Correct!")
else:
    print("Wrong! The number was", secret)
```

### Concepts Used

* Random Module
* User Input
* Conditions
* Variables

---

# 🧠 Concepts Covered Today

✅ Print Statements
✅ Variables & Data Types
✅ User Input
✅ Arithmetic Operators
✅ Conditional Statements
✅ While Loop
✅ For Loop
✅ Lists
✅ Functions
✅ Return Statement
✅ Mini Project – Number Guessing Game

---

# 📌 Day 0 Complete

Python Mastery – 100 Days, 100 Projects 🚀
