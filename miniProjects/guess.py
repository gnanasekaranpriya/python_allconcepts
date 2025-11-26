#1. Guessing Game 
# Description:
# The program picks a random number between 1–100.
# The user has to guess it.
# After each guess, tell the user if it’s too high or too low.
# Count the number of attempts and display it at the end.
# Wrap the guessing logic inside a function.

from random import randint 

num = randint(1, 50)
guess = int(input('Guess a number: '))
l = 0

while guess != num:
    if l < 10:
        guess = int(input('Guess another number: '))
    else: 
        print('You ran out of guess!')
        break
    l += 1
print('You got it correct')












