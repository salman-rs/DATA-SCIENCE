import secrets

import random

secret_number = random.randint(1,100)
guess = 0
print("I am thinking of a number between 1 and 10,can you guess it:")
while guess != secret_number:
 guess = int(input("enter your guess:"))
if guess < secret_number:
    print("too low,try again")
elif guess > secret_number:
    print("too high,try again")
else:
    print("you guessed correctly")
