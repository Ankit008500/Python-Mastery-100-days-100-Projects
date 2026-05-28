python
# Python Mastery - Day 0
# Quick Revision Practice

# Print Statement
print("Hello World")


# Variables and Data Types
name = "Ankit"
age = 20
height = 5.8
is_student = True

print(name)
print(age)
print(height)
print(is_student)


# User Input
user_name = input("Enter your name: ")

print("Welcome", user_name)


# Arithmetic Operators
x = 10
y = 3

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Power:", x ** y)


# Conditional Statements
user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("Adult")
elif user_age >= 13:
    print("Teenager")
else:
    print("Child")


# While Loop
count = 0

while count < 5:
    print("Count:", count)
    count += 1


# For Loop
games = ["Minecraft", "Valorant", "GTA"]

for game in games:
    print(game)


# Lists
games.append("BGMI")

print(games)
print(games[0])


# Functions
def greet(name):
    print("Hello", name)

greet("Ankit")


# Return Statement
def multiply(a, b):
    return a * b

result = multiply(5, 10)

print(result)


# Mini Project - Number Guessing Game
import random

secret = random.randint(1, 10)

guess = int(input("Guess the number between 1 and 10: "))

if guess == secret:
    print("Correct!")
else:
    print("Wrong! The number was", secret)
```

