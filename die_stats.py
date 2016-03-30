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

# while 0 < number_of_dice:
# 	die_roll = randint(1, 6)
# 	print("Dice rolled: ", die_roll)
	
# 	sum_of_dice += die_roll
# 	roll_list = [print(roll) for roll in die_roll]
# 	print(roll_list)
# 	# Decrement number of dice so while loop knows to stop
# 	number_of_dice -= 1
# print("Total sum of dice rolled: ", sum_of_dice)
# mean_of_rolls = sum_of_dice / total_dice
# print("Mean: ", mean_of_rolls)
# min_roll_num = min(die_roll_list)
# print("Minimum roll: ", min_roll_num)
# max_roll_num = 

# roll_list = list(range(1, (total_dice + 1)))
# print(roll_list)

roll_list = [randint(1, 6) for roll in range(1, (total_dice + 1))]
print("Here are the numbers you rolled: ", roll_list)

sum_of_rolls = 0

while total_dice > 0:
	sum_of_rolls += roll_list[total_dice - 1]
	total_dice -= 1
	mean_of_rolls = sum_of_rolls / number_of_dice

print("The sum of the rolls is: ", sum_of_rolls)
print("The mean of the rolls is: ", mean_of_rolls)

min_roll_num = min(roll_list)
print("The smallest number rolled was ", min_roll_num)

max_roll_num = max(roll_list)
print("The highest number rolled was ", max_roll_num)



