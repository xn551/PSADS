# Design a class to represent a playing card. Now design a class to represent a deck of cards. Using these two classes, implement a favorite card game.
## a playing card
#* Pattern: Hearts Diamonds Clubs Spades Joker
#* Number: 1~10, J, Q, K, small Joker, big Joker

import random

pa_value_name_list = ['Heart','Dimond','Spades','Clubs']
no_value_name_list = ['A'] + [str(i) for i in (range(2,11))] + ['J'] + ['Q'] + ['K'] 

class a_card:
	def __init__(self,Pa_name,No_name):
		self.No_name = No_name
		self.Pa_name = Pa_name

	def getHash(self):
		global pa_value_name_list
		global no_value_name_list
		if self.Pa_name != "Joker":
			self.No = no_value_name_list.index(self.No_name) + 1
			self.Pa = pa_value_name_list.index(self.Pa_name) + 1
			self.hash = (self.No - 1) * 4 + self.Pa 
		else:
			if self.No_name == "small":
				self.hash = 53
			else:
				self.hash = 54
		return self.hash
	
	def getValue(self):
		global pa_value_name_list
		global no_value_name_list
		if self.Pa_name != "Joker":
			self.No = no_value_name_list.index(self.No_name) + 1
			self.Pa = pa_value_name_list.index(self.Pa_name) + 1
			if self.No in range(3,14):
				self.value = self.No - 2
			if self.No in range(1,3):
				self.value = self.No + 11
		else:
			if self.No_name == "small":
				self.value = 14
			else:
				self.value = 15
		return self.value
		

class deck_cards:
	def __init__(self):
		self.state = list(range(1,55))

	def shuffle(self):
		random.shuffle(self.state)

	def deal(self):
		self.A = self.state[slice(1,55,2)]
		self.B = self.state[slice(2,55,2)]
		self.A.sort()
		self.B.sort()
		return [ self.A, self.B ]

	def card_is(self,card_hash):
		pa = card_hash % 4
		if pa == 0:
			pa = 4
		no = card_hash // 4 + 1
		if pa == 4:
			no = no -1
		global pa_value_name_list
		global no_value_name_list
		if card_hash < 52:
			pa_name = pa_value_name_list[pa-1]
			no_name = no_value_name_list[no-1]
		elif card_hash == 52:
			pa_name = 'Clubs'
			no_name = 'K'
		elif card_hash == 53:
			pa_name = 'Joker'
			no_name = 'small'
		elif card_hash == 54:
			pa_name = 'Joker'
			no_name = 'big'
		return [ pa_name, no_name ] 

	def show_cards(self, card_hash_list):
		i = 1
		for card_hash in card_hash_list:
			card_name = self.card_is(card_hash)
			print("| No.",i,' ', card_name[0],' ', card_name[1],  end='')
			i += 1
		print("|")

class rule:
	def __init__(self, A_cards, B_cards):
		self.turns = None
		self.last_no = None
		self.last_pa = None
		self.last_cardN = None
		self.last_value = 0
		self.A_cards = A_cards
		self.B_cards = B_cards
		self.win = None

	def who_is_first(self):
		if a_card("Heart","3").getHash() in self.A_cards:
			self.turns = "A"
		else:
			self.turns = "B"

	def nextOne(self):
		if self.turns == "A":
			return "B"
		else:
			return "A"
	def sort(self, A_cards):
		A_cards.sort()

	def deal_card(self):
		turns = self.turns
		print("\n This is", turns, "turn")
		if turns == "A":
			cards_set = A_cards
		else:
			cards_set = B_cards
		cards_set.sort()
		print("last value is ", self.last_value)
		print("last card is ", self.last_pa,' ', self.last_no)
		while True:
			list_no = input("Deal your card: ")
			list_no = list_no.split()
			element_no = len(list_no)
			print("shelf.last_cardN",self.last_cardN)

			if self.last_cardN != None:
				if element_no != self.last_cardN:
					print(" the number of cards should be",self.last_cardN)
				else:
					if self.last_cardN == 1:
						Hash = cards_set[ int(list_no[0]) - 1]
						cardIs = deck_cards().card_is(Hash)
						Pa = cardIs[0]
						No = cardIs[1]

						print(Pa,' ', No)

						if list_no[0] == '0':
							self.turns = self.nextOne()
							self.last_value = 0
							self.last_no = None
							self.last_pa = None
							self.last_cardN = None
							return

						Hash = a_card(Pa,No).getHash()
						print (cards_set)
						print( Hash)
						if Hash not in cards_set:
							print("You do not have the card")
							continue

						if a_card(Pa,No).getValue() <= self.last_value:
							print("Your card is smaller than last one")
							continue

						cards_set.remove(Hash)
						print(cards_set)
						self.last_value = a_card(Pa,No).getValue()
						self.last_no = No
						self.last_pa = Pa
						
						break

					if self.last_cardN == 2:
						if list_no[0] == list_no[1]:
							print("deal two same cards")
							continue
						
						Hash = [0,0]
						cardIs = [0,0]
						Pa = [0, 0]
						No = [0, 0]
						

						Hash[0] = cards_set[ int(list_no[0]) - 1]
						cardIs[0] = deck_cards().card_is(Hash[0])
						Pa[0] = cardIs[0][0]
						No[0] = cardIs[0][1]

						Hash[1] = cards_set[ int(list_no[1]) - 1]
						cardIs[1] = deck_cards().card_is(Hash[1])
						Pa[1] = cardIs[1][0]
						No[1] = cardIs[1][1]

						print(Pa[0],' ', No[0], end ='')
						print(Pa[1],' ', No[1], end ='')

						if list_no[0] == '0':
							self.turns = self.nextOne()
							self.last_value = 0
							self.last_no = None
							self.last_pa = None
							self.last_cardN = None
							return

						print (cards_set)
						print( Hash[0], Hash[1])

						if Hash[0] not in cards_set:
							print("You do not have the card")
							continue

						if Hash[1] not in cards_set:
							print("You do not have the card")
							continue

						if a_card(Pa[0],No[0]).getValue() != a_card(Pa[1],No[1]).getValue():
							print("Your two card are different!")
							continue
						
						if a_card(Pa[0],No[0]).getValue() <= self.last_value[0]:
							print("Your card is smaller than last one")
							continue
						
						cards_set.remove(Hash[0])
						cards_set.remove(Hash[1])
						print(cards_set)
						self.last_value[0] = a_card(Pa[0],No[0]).getValue()
						self.last_value[1] = a_card(Pa[1],No[1]).getValue()
						self.last_no[0] = No[0]
						self.last_pa[1] = Pa[1]
						self.last_no[1] = No[1]
						self.last_pa[0] = Pa[0]
						
						break

			if self.last_cardN == None:
					if element_no == 1:
						Hash = cards_set[ int(list_no[0]) - 1]
						cardIs = deck_cards().card_is(Hash)
						Pa = cardIs[0]
						No = cardIs[1]

						print(Pa,' ', No)

						if list_no[0] == '0':
							self.turns = self.nextOne()
							self.last_value = 0
							self.last_no = None
							self.last_pa = None
							self.last_cardN = None
							return

						Hash = a_card(Pa,No).getHash()
						print (cards_set)
						print( Hash)
						if Hash not in cards_set:
							print("You do not have the card")
							continue
						if a_card(Pa,No).getValue() <= self.last_value:
							print("Your card is smaller than last one")
							continue
						

						cards_set.remove(Hash)
						print(cards_set)
						self.last_value = a_card(Pa,No).getValue()
						self.last_no = No
						self.last_pa = Pa

						break

					if element_no == 2:
						if list_no[0] == list_no[1]:
							print("deal two same cards")
							continue

						Hash = [0,0]
						cardIs = [0,0]
						Pa = [0, 0]
						No = [0, 0]
						self.last_value =[0, 0] 
						self.last_no = [0, 0]
						self.last_pa = [0, 0]
						Hash[0] = cards_set[ int(list_no[0]) - 1]
						cardIs[0] = deck_cards().card_is(Hash[0])
						Pa[0] = cardIs[0][0]
						No[0] = cardIs[0][1]

						Hash[1] = cards_set[ int(list_no[1]) - 1]
						cardIs[1] = deck_cards().card_is(Hash[1])
						Pa[1] = cardIs[1][0]
						No[1] = cardIs[1][1]

						print(Pa[0],' ', No[0], end ='')
						print(Pa[1],' ', No[1], end ='')

						if list_no[0] == '0':
							self.turns = self.nextOne()
							self.last_value = 0
							self.last_no = None
							self.last_pa = None
							self.last_cardN = None
							return

						print (cards_set)
						print( Hash[0], Hash[1])

						if Hash[0] not in cards_set:
							print("You do not have the card")
							continue

						if Hash[1] not in cards_set:
							print("You do not have the card")
							continue

						if a_card(Pa[0],No[0]).getValue() != a_card(Pa[1],No[1]).getValue():
							print("Your two card are different!")
							continue
						
						if a_card(Pa[0],No[0]).getValue() <= self.last_value[0]:
							print("Your card is smaller than last one")
							continue
						
						cards_set.remove(Hash[0])
						cards_set.remove(Hash[1])
						print(cards_set)
						self.last_value[0] = a_card(Pa[0],No[0]).getValue()
						self.last_value[1] = a_card(Pa[1],No[1]).getValue()
						self.last_no[0] = No[0]
						self.last_pa[1] = Pa[1]
						self.last_no[1] = No[1]
						self.last_pa[0] = Pa[0]
						self.last_cardN = 2
						break

		if turns == "A":
			self.A_cards = cards_set
		else:
			self.B_cards = cards_set
		self.turns = self.nextOne()
	
	def whoWin(self):
		if self.A_cards == []:
			self.win = "A"
			print ("A win!")
			return self.win
		elif self.B_cards == []:
			self.win = "B"
			print("B win!")
			return self.win
		else:
			self.win = None
			return self.win


one_cards = deck_cards()
one_cards.shuffle()
deal_cards = one_cards.deal()

A_cards = deal_cards[0]
B_cards = deal_cards[1]

one_game = rule(A_cards,B_cards)
one_game.who_is_first()
while True:
	if one_game.turns == "A":
		one_cards.show_cards(A_cards)
	else:
		one_cards.show_cards(B_cards)

	one_game.deal_card()

	if one_game.whoWin() != None:
		break
	
