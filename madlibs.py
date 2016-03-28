"""Make a simple madlib, you can look one up. Ask for three words, save them in variables, fill in the madlib, then print the final madlib."""

# Create a variable for each word the user must input via input prompt
word1_person = input("Please enter a person: ")
word2_person = input("Please enter another person: ")
word3_noun = input("Please enter a noun: ")
word4_plural_noun = input("Please enter a plural noun: ")
word5_place = input("Please enter a place: ")

# The madlib passage, using string concatination to put the variables (user input) at the appropriate places
madlib = "Tennis News: The Miami Open\nSeemingly in control of his opening match at the Miami Open on Saturday, " + word1_person + " fell ill and promptly retired against No. 94 " + word2_person + ". It was a disappointment for the fifth-ranked " + word3_noun + ", who has always enjoyed playing in front of his large contingent of " + word4_plural_noun + " in " + word5_place + "."

# Print completed madlib with user's word choices
print(madlib)