import random

secret_number = random.randint(1, 10)

guess = 0

while not (guess == secret_number):
    guess = int(input("Guess the number: "))

    if guess < secret_number:
        print("Too Low")
    elif guess > secret_number:
        print("Too High")
    else:
        print("Correct")

# OOP
# Object Oriented Programming
# Four Pillars of OOP