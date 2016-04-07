""" Create a program that scores a hand of Black Jack """

# Dictionary to establish all faces possible and their associated values in a game of blackjack specifically, since values might be different for another card game.
blackjack_value_dict = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

# List of possible suits in a standard deck of cards
suit_list = ["Hearts", "Clubs", "Spades", "Diamonds"]

# Class that represents a card.
class Card:

	def __init__(self, face, suit):
		# You don't need a value attribute here, like I originally thought I might, because the values technically only apply to the specific card game you are playing, which in this case is blackjack. The values can change, depending on the card game you're playing, and it's better to create a simpler card class for modularization purposes - that way, it encompasses only the two necessary attributes for a standard playing card and thus doesn't further complicate things with blackjack specific paramaters (e.g. card value) and you can use the card class for a different card game program in the future, yay!
		self.face = face
		self.suit = suit

	def get_blackjack_card_value(self):
		if self.face in blackjack_value_dict:
			card_value = blackjack_value_dict[self.face]
			return card_value
		

	def __repr__(self):
		# You can only technically return one thing, so the way I had it written before with an and statement (return self.face and self.suit) didn't work because Python will only return one of those. Use .format here instead to be able to include multiple attributes of the Class. The squiggly brackets (a.k.a. curly braces) each represent individually represent the arguments in the parentheses after the .format. Thus, self.face appears within the string where the first set of curly braces are and then self.suit appears where the second set of curly braces are. There is an "of" within the string just so it prints out all pretty and proper for these specific circumstances, meaning because it is a card, it will say Queen of Hearts instead of just Queen Hearts. 
		return "{} of {}".format(self.face, self.suit)

# 2. Make a Class that represents a hand of cards.
class Hand:

	def __init__(self):

		# self.card = Card() <--- Note to self: don't do this, your code will break. Python just doesn't work like that!
		# Created an empty list to initialize card_hand_list because it technically starts as empty anyway but is still a hand, if you get my drift, which is why you technically don't need to initialize a card attribute because in computer programming world and in this case, the hand can exist with nothing in it technically and that is how it starts anyway.
		self.card_hand_list = []

	# Function that adds a card to a hand. Must pass card as an argument because, given the definition of a function, a card will be passed into the add_card function no matter what because obviously that's the purpose of the function.
	def add_card(self, card):
		self.card_hand_list.append(card)

	# Function that scores a hand
	def score_hand(self, card):
		for card in self.card_hand_list:
		 	card_score = sum(self.card_hand_list)
		pass

	def __repr__(self):

		# Need to stringify the return or else an error pops up because it is a list and the magic repr function is expecting to return a string.
		return str(self.card_hand_list)

# Maybe do a score card function as well as a score hand function??
def card_value(card):

	pass

# Function that alerts that hand is now over 21
def over_21_alert():
	pass


# 4. Allow a user to type in a hand and have it be converted into card objects and then scored

# I think I will need a function that randomly selects a card for the user. Or wait...is that getting ahead of myself and that would be a function once I create a deck of cards

# This is just some hard coding for testing purposes
a_card = Card("Queen", "Hearts")
# print(a_card)

another_card = Card("Ace", "Clubs")

a_hand = Hand()
# print(a_hand)

a_hand.add_card(a_card)
print(a_hand)

# a_hand.add_card(another_card)
# print(a_hand)

print(another_card.get_blackjack_card_value())

