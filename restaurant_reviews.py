""" Practice: Restaurant Reviews - assignment to create a mini version of Yelp """

raw_business_review_data = [
  {
    'business_name': 'Salt & Straw',
    'reviews': [
      {'rating': 5, 'text': 'Luscious ice cream!'},
      {'rating': 4, 'text': 'Super tasty, but such a long line!'},
      {'rating': 2, 'text': 'Overrated, but I like sugar.'}
    ],
  },
  {
    'business_name': 'Voodoo Donuts',
    'reviews': [
      {'rating': 1, 'text': 'I do not like bubblegum on my donuts.'},
      {'rating': 5, 'text': 'Pink building is so cute!'},
      {'rating': 2, 'text': 'Diabetes inducing.'}
    ],
  },
]

class Review:

	def __init__(self, rating, review_text):

		self.rating = rating
		self.review_text = review_text

	def __repr__(self):

		return self.rating and self.review_text

# Write a function that can turn this data into an instance of a Class:
single_review_dict = {'rating': 5, 'text' : "Luscious ice cream!"}

class Business:

	def __init__(self, business_name, review):

		self.business_name = business_name
		self.review = review

	def get_business_reviews(self):
		business_reviews = self.business_name + str(review.rating) + review.review_text

		return business_reviews
		print(business_reviews)


	def __repr__(self):

		return self.business_name and self.review
		print(self.business_name, self.review)


voodoo = Business("Voodoo Donuts: ", "here is a review")
# voodoo.business_name = "Voodoo Donuts: "
# voodoo.review = "here is a review."

print(voodoo)

