import cards
from random import shuffle

class Deck():

	value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
	suit = ['Heart', 'Diamonds', 'Clubs', 'Spades']

	def __init__(self):
		self.count = 52
		self.cards = []
		for s in Deck.suit:
			for v in Deck.value:
				self.cards.append(cards.Card(s, v))

	def __repr__(self):
		return f"Deck of {self.count}"

	def _deal(self, num):
		deal = []
		while num != 0:
				deal.append(self.cards.pop())
				num -= 1
				self.count -= 1
			if self.count <= 0: raise ValueError("All cards have been delt")
		return deal

	def shuffle(self):
		if self.count<52:
			raise ValueError("Only full decks can be shuffled")
		return shuffle(self.cards)

	def deal_card(self):
		return Deck._deal(1)[0]

	def deal_hand(self, hand_size):
		return Deck._deal(hand_size)

deck1 = Deck()
print(deck1)
deck1.shuffle()
print(deck1._deal(3))
# deck1.deal_hand(2)
# print(deck1)
# # print(deck1.deal_card())
# print(deck1)