# Python Mastery – Day 0

## Quick Revision of Python Fundamentals

---

## Print Statement

```python id="4t4tud"
print("Hello World")
```

### Output

```python id="1wq9hl"
Hello World
```

### Purpose

Used to display output on the screen.

---

## Variables and Data Types

```python id="ydm8ux"
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

## User Input

```python id="9t8g7r"
name = input("Enter your name: ")

print("Welcome", name)
```

### Purpose

Used to take input from the user.

---

## Arithmetic Operators

```python id="uh8l78"
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

## Conditional Statements

```python id="pqsbvq"
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

## While Loop

```python id="j3p18d"
count = 0

while count < 5:
    print(count)
    count += 1
```

### Purpose

Repeats code while condition is True.

---

## For Loop

```python id="0i6rly"
games = ["Minecraft", "Valorant", "GTA"]

for game in games:
    print(game)
```

### Purpose

Used to iterate through items.

---

## Lists

```python id="o0mpul"
games = ["Minecraft", "Valorant", "GTA"]

print(games[0])

games.append("BGMI")

print(games)
```

### Output

```python id="v69vv6"
['Minecraft', 'Valorant', 'GTA', 'BGMI']
```

### Purpose

Stores multiple values in one variable.

---

## Functions

```python id="jk2msp"
def greet(name):
    print("Hello", name)

greet("Ankit")
```

### Purpose

Reusable block of code.

---

## Return Statement

```python id="l7y0jr"
def multiply(a, b):
    return a * b

result = multiply(5, 10)

print(result)
```

### Output

```python id="22pkju"
50
```

### Purpose

Returns value from a function.

---

## Mini Project – Number Guessing Game

```python id="el6o2t"
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

## Concepts Covered

* Print Statements
* Variables and Data Types
* User Input
* Arithmetic Operators
* Conditional Statements
* While Loop
* For Loop
* Lists
* Functions
* Return Statement
* Number Guessing Game
