from deck import Deck, Card

class PokerHand:
    def __init__(self, deck):

        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self._cards)

    @property
    def is_flush(self):
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit: # comparing 1st card suit to every other card suit
                return False
        return True

    @property
    def number_of_matches(self):
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        if self.number_of_matches == 2:
            return True
        return False

    @property
    def is_two_pair(self):
        return self.number_of_matches == 4 # more complicated method
# ^ shorter; returns True when conditional satisfied & if not, automatically False

    @property
    def is_three_pair(self):
        return self.number_of_matches == 6

    @property
    def is_four_pair(self):
        return self.number_of_matches == 12

# Full house = if is_three_pair & is_two_pair
    @property
    def is_full_house(self):
        return self.number_of_matches == 8

    @property
    def is_straight(self):
        self.cards.sort()
        distance = Card.RANKS.index(self.cards[4].rank) - \
                   Card.RANKS.index(self.cards[0].rank)
        return self.number_of_matches == 0 and distance == 4

count = 0
matches = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_straight:
        matches += 1
        print(hand)
    count += 1

print(f"Probability of a straight flush is {100*matches/count}%")

# Probability of each type of pair:
# single pair ~ 42.405% (10k)
# two pair ~ 4.719% (10k)
# three pair ~ 2.091% (10k)
# four pair ~ 0.026% (100)
# full house ~ 0.146% (1k)
# straight flush ~ 0.351% (1k)
