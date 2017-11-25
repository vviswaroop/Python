#This is the guess number game

import random

print('Hello, What is your name?')
name = raw_input()



secretNumber = random.randint(1, 20)

print('Well ' + name + ', I am thinking of a number between 0 and 20')
for guessesTaken in range(1, 7):
	print('Take a guess')
	guess = int(input())

	if guess < secretNumber:
		print('guess is too low')
	elif guess > secretNumber:
		print('guess id too high')
	else:
		 break #break condition

if guess == secretNumber:
	print('good job ' + name )

print(' you took + str(guessesTaken) + guesses.')
