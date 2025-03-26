import random

class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♠️", "♥️", "♦️", "♣️"]
    def __init__(self, suit, rank):
        if rank not in self.RANKS:
            raise ValueError("Invalid Rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid Suit")
        self._rank = rank
        self._suit = suit

    def __eq__(self, other):
        return self.rank == other.rank

    def __gt__(self, other):
        """
        Compares position of 'self' & 'other' in RANKS list
        :param other:
        :return:
        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __str__(self): # str for when it will be put in a normal string
        return f"{self._rank}{self._suit}"

    def __repr__(self): # use repr for when it will be put in a list
        return self.__str__()

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

class Deck:
    def __init__(self):
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit, rank))

    def __str__(self):
        return str(self._deck)

    def shuffle(self):
        random.shuffle(self._deck)

    def deal(self):
        return self._deck.pop(0)

if __name__ == "__main__":
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())