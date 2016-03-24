# Word Count Assignment: 
	# Count how often each unique word is used, then print the most frequent top 10 out with their counts
	# Count how often each unique pair of words is used, then print the most frequent top 10 out with their counts

# 1. Create list of words from text
# - loop through text (for loop) to make a list of words
# Loop through entire text to get list of every word used in text
import re
# Open text document version of The Odyssey
with open("odyssey.txt") as odyssey_file:
	# Use readlines function instead of read function. This will create a list of strings from the book lines
	odyssey_text = odyssey_file.read()


odyssey_word_list = str(odyssey_text).split()

# print(odyssey_word_list)
# before creating list, remove new lines, punctuation, caps, etc.
# new_line_removal = odyssey_string_text.replace('\n', ' ')
# new_line_removal = re.sub("\n", "", odyssey_string_text)

for word in odyssey_word_list:
		word_sans_punctuation = word.strip(',.:;?"!()')
		# print(word_sans_punctuation)

		lower_case_word = word_sans_punctuation.lower()

		print(lower_case_word)













# for word in word_list:
# 	word_list.count(x)

# create dictionary with word as key and the number of instances as the value


