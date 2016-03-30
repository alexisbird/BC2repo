"""Ask the user how many 6-sided dice they should roll. Roll that many. Print the mean, min, and max values."""

# Import random integer built-in Python function
from random import randint

# Variable to store user's input for how many dice they want to roll
number_of_dice = int(input("How many dice would you like to roll? "))

# Variable to store value to later use for decrementing specifically and then still maintain value for number_of_dice
total_dice = number_of_dice

# Create list of numbers rolled by dice through randint occurring for each instance in range 1 to number of dice being rolled (added 1 to account for the last number not being included with range function) via  a for loop, then surrounded it by square brackets to make it a list
roll_list = [randint(1, 6) for roll in range(1, (total_dice + 1))]
# Print statement primarily for testing purposes but also for user to see
print("Here are the numbers you rolled: ", roll_list)

# Set sum_of_rolls to initial value of 0 to create variable and be able to add to it later
sum_of_rolls = 0

# While loop to calculate the sum and the mean of all the rolls
while total_dice > 0:
	sum_of_rolls += roll_list[total_dice - 1]
	total_dice -= 1
	mean_of_rolls = sum_of_rolls / number_of_dice
# More print statements to help test and also display for user
print("The sum of the rolls is ", sum_of_rolls)
print("The mean of the rolls is ", mean_of_rolls)

min_roll_num = min(roll_list)
print("The smallest number rolled was ", min_roll_num)

max_roll_num = max(roll_list)
print("The highest number rolled was ", max_roll_num)



