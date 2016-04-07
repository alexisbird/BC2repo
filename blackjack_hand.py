""" Create a program that scores a hand of Black Jack """

face_value_dict = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}

suit_list = ["Hearts", "Clubs", "Spades", "Diamonds"]

# 1. Make a Class that represents a card.
class Card:

	def __init__(self, suit, face):

		self.suit = suit
		self.face = face
		

	def __repr__(self):
		# You can only technically return one thing, so the way I had it written before with an and statement (return self.face and self.suit) didn't work because Python will only return one of those. Use .format here instead to be able to include multiple attributes of the Class. The squiggly brackets (a.k.a. curly braces) each represent individually represent the arguments in the parentheses after the .format. Thus, self.face appears within the string where the first set of curly braces are and then self.suit appears where the second set of curly braces are. There is an "of" within the string just so it prints out all pretty and proper for these specific circumstances, meaning because it is a card, it will say Queen of Hearts instead of just Queen Hearts. 
		return "{} of {}".format(self.face, self.suit)

# 2. Make a Class that represents a hand of cards.
class Hand:

	def __init__(self):

		# self.card = Card() <--- Note to self: don't do this, your code will break
		# Created an empty list to initialize card_hand_list because it technically starts as empty anyway but is still a hand, if you get my drift
		self.card_hand_list = []

	# Function that adds a card to a hand. Must pass card as an argument
	def add_card(self, card):
		self.card_hand_list.append(card)
		# Print statement for the time being for testing purposes


	def __repr__(self):

		return str(self.card_hand_list)

# Function that scores a hand
def score_hand():
	pass

# Function that alerts that hand is now over 21
def over_21_alert():
	pass


# 3. Add functions that:
		# - add a card to a hand
		# - score a hand
		# - return if score is over 21

# 4. Allow a user to type in a hand and have it be converted into card objects and then scored

# I think I will need a function that randomly selects a card for the user. Or wait...is that getting ahead of myself and that would be a function once I create a deck of cards
a_card = Card("Hearts", "Queen")
print(a_card)

a_hand = Hand()
print(a_hand)

a_hand.add_card(a_card)
print(a_hand)


