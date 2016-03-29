"""Ask the user how many 6-sided dice they should roll. Roll that many. Print the mean, min, and max values."""

# Generate random number from 1 to 6 for dice roll
# Ask user how many dice to roll
# Roll the dice that many times
#

# Import random integer built-in Python function
from random import randint

# Variable to store user's input for how many dice they want to roll
number_of_dice = int(input("How many dice would you like to roll? "))
total_dice = number_of_dice
sum_of_dice = 0

while 0 < number_of_dice:
	die_roll = randint(1, 6)
	print("Dice rolled: ", die_roll)
	
	sum_of_dice += die_roll
	# Decrement number of dice so while loop knows to stop
	number_of_dice -= 1
print("Total sum of dice rolled: ", sum_of_dice)
mean_of_rolls = sum_of_dice / total_dice
print("Mean: ", mean_of_rolls)
# min_roll_num = min(die_roll_list)
# print("Minimum roll: ", min_roll_num)
# max_roll_num = 








