"""Have the program generate a random int between 1 and 100. Keep it a secret. Ask the user to guess. Tell them if the secret number is higher or lower than their guess. Let them guess until they get it right.

Advanced:

Limit the number of guesses to 5."""

# ***NOTE TO SELF*** if you have the time and desire:
# - Add a quit function
# - Add an option to play again at end of game

# Import built-in Python function randint to generate a random integer
from random import randint

# Randomly generate a secret number between 1 and 100
secret_number = randint(1, 100)
# Make into string to keep things clean, so to speak (easier comparison options, game doesn't break when user enters a letter or word)
secret_number_string = str(secret_number)

# this is just for testing purposes
print(secret_number)

# Establish initial value for user's guess number as 1
guess_number = 1

# Initial print statement to explain the game
print("\nThe computer has randomly selected a number between 1 and 100. Enter a number to guess what it is. You have 5 guesses total. ")

# While loop to limit number of guesses
while guess_number < 5:
	# Ask user to guess a number, convert to integer so computer knows it's a number
	user_guess = input("\nPlease guess a number. ")
	# If statement to determine if user has won
	# If statement determines what happens in the event that the user guesses correctly
	if user_guess == secret_number_string:
		print("That is correct! You win!")
		exit()
	# Elif statement determines what happens if the user guesses incorrectly
	elif user_guess != secret_number_string:
		# Variable for remaining guesses so that user knows how many guesses they have left: 5 (max number of guesses) minus the number of the guess that the user is currently on equals the remaining number of guesses
		remaining_guesses = 5 - guess_number
		# If statement within if statement to specify if guess should be printed plurally or singularly because I'm a weird grammar Nazi like that
		# If specifies that it is guesses since it will be plural if the number is greater than 1
		# stringify the number so you can concatinate it
		if remaining_guesses > 1:
			print("Nope. Keep guessing! You have " + str(remaining_guesses) + " guesses left. ")
		# Elif specifies that guess is singular when it is 1
		elif remaining_guesses == 1:
			print("Nope. Keep guessing! You have " + str(remaining_guesses) + " guess left. ")
	# Increment number of guesses each time we loop through to limit number of guesses
	guess_number += 1

# If statement to account for when user is on the very last guess, guess #5, primarily for the purpose of alerting user if they have completely lost the game
if guess_number == 5:
	user_guess = input("\nPlease guess a number. ")

	if user_guess == secret_number_string:
		print("That is correct! You win!")

	else:
		print("Incorrect and out of guesses! Game over. You get nothing! You lose! Good day, sir (or madame)! ")
		exit()



