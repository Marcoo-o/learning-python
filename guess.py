import random

guess = 0
test = random.randint(1,2)

while guess != test:
  guess = int(input("Guess the number:  "))

print("You got it!")