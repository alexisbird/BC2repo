""" Practice Assignment: ATM

Write a program that functions as a simple ATM for a single account. 

An account will be a Class: it will have a field for the balance.

Write functions for the account class that:
- Deposit to the account
- Check if enough funds for a withdrawal
- Withdraw an allowed amount
- Calculate 0.5 percent interest on the account

Implement a user interface that lets the user pick each of those actions and update the account. After each action, it will print the balance. """

class Account:

	def __init__(self, name, balance, deposit, withdrawal, interest):

		self.name = name # Or empty string????
		self.balance = 0 # Or should this be just balance instead of 0?
		self.deposit = 0
		self.withdrawal = 0
		self.interest = 0.5 # Maybe change this to 0.005 because it's a percent

	def deposit_funds(self):
		pass

	def check_balance(self):
		pass

	def calc_interest(self):
		pass

	def withdraw_funds(self):
		pass

	# Maybe another function for updating? Would that be necessary?

	def __str__(self):

		return self.balance
		


