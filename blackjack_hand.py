""" Create a program that scores a hand of Black Jack """

# 1. Make a Class that represents a card.
class Card:

	def __init__(self, suit, face, value):

		self.suit = suit
		self.face = face
		self.value = value

	def determine_card_value(self):
		
		

	def __repr__(self):
		return self.suit and self.face

# 2. Make a Class that represents a hand.
class Hand:

	def __init__(self, card, card_hand):

		self.card = Card()
		self.card_hand_list = [Card()]

	# Function that adds a card to a hand
	def add_card(self):
		current_card_list = self.card_hand_list.append(self.card)
		# Print statement for the time being for testing purposes
		print(current_card_list)


	def __repr__(self):

		return self.card_hand_list

# Function that scores a hand
def score_hand():
	face_value_dict = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}
	suit_list = ["Hearts", "Clubs", "Spades", "Diamonds"]

# Function that alerts that hand is now over 21
def over_21_alert():

	pass


# 3. Add functions that:
		# - add a card to a hand
		# - score a hand
		# - return if score is over 21

# 4. Allow a user to type in a hand and have it be converted into card objects and then scored

# I think I will need a function that randomly selects a card for the user. Or wait...is that getting ahead of myself and that would be a function once I create a deck of cards
