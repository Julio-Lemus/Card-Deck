class Card():
	def __init__(self, s, v):
		self.suit = s
		self.value = v
	
	def __repr__(self):
		return f"{self.value} of {self.suit}"