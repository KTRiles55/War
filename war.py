# War Card Game
import random

suits = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        print(f'{self.rank} of {self.suit}')


class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle_cards(self):
        random.shuffle(self.all_cards)

    def deal_cards(self):
        return self.all_cards.pop()


new_deck = Deck()

new_deck.shuffle_cards()


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)

        else:
            self.all_cards.append(new_cards)

    def remove_card(self):
        return self.all_cards.pop(0)


player_one = Player('Kenny')

player_two = Player('Cpu')

for x in range(26):
    player_one.add_cards(new_deck.deal_cards())
    player_two.add_cards(new_deck.deal_cards())

game = True
round = 0
while game:
    round += 1
    print(f'...Round {round}...')

    if len(player_one.all_cards) == 0:
        print('Player 1 loses! Player 2 wins!')
        game = False
        break

    if len(player_two.all_cards) == 0:
        print('Player 2 loses! Player 1 wins!')
        game = False
        break

    player_one_hand = []
    player_one_hand.append(player_one.remove_card())

    player_two_hand = []
    player_two_hand.append(player_two.remove_card())

    war_on = True

    while war_on:

        if player_one_hand[-1].value > player_two_hand[-1].value:
            player_one.add_cards(player_one_hand)
            player_one.add_cards(player_two_hand)
            war_on = False

        elif player_one_hand[-1].value < player_two_hand[-1].value:
            player_two.add_cards(player_two_hand)
            player_two.add_cards(player_one_hand)
            war_on = False

        else:
            print('It is War!')

            if len(player_one.all_cards) < 5:
                print('Player 1 cannot fight in war! Player 2 wins!')
                game = False
                break
            elif len(player_two.all_cards) < 5:
                print('Player 2 cannot fight in war! Player 1 wins!')
                game = False
                break

            else:
                for num in range(5):
                    player_one_hand.append(player_one.remove_card())
                    player_two_hand.append(player_two.remove_card())
