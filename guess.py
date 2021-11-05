# Basic guessing game
from random import randint

for i in range(10):
    secret = randint(0, 10)

print(secret)


while True:
    guess = int(input("Guess a number between 0-10: "))
    if secret == guess:
        print("You are correct!")
        exit()
    elif guess > secret:
        print("Your guess was to high")
    else:
        print("Your guess was to low")
