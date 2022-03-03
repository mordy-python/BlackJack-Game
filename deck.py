from random import shuffle


class Deck:
    def __init__(self):

        self.nums = [
            "ace",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten",
        ]
        self.deck = []
        self.__create_diamonds()
        self.__create_spades()
        self.__create_hearts()
        self.__create_clubs()
        shuffle(self.deck)

    def __create_diamonds(self):
        diamonds = []
        for val in range(1, 11):
            diamonds.append(Card(val, self.nums[val - 1], "diamonds"))
        diamonds.append(Card(10, "jack", "diamonds"))
        diamonds.append(Card(10, "queen", "diamonds"))
        diamonds.append(Card(10, "king", "diamonds"))
        self.deck += diamonds
        return diamonds

    def __create_hearts(self):
        hearts = []
        for val in range(1, 11):
            hearts.append(Card(val, self.nums[val - 1], "hearts"))
        hearts.append(Card(10, "jack", "hearts"))
        hearts.append(Card(10, "queen", "hearts"))
        hearts.append(Card(10, "king", "hearts"))
        self.deck += hearts
        return hearts

    def __create_spades(self):
        spades = []
        for val in range(1, 11):
            spades.append(Card(val, self.nums[val - 1], "spades"))
        spades.append(Card(10, "jack", "spades"))
        spades.append(Card(10, "queen", "spades"))
        spades.append(Card(10, "king", "spades"))
        self.deck += spades
        return spades

    def __create_clubs(self):
        clubs = []
        for val in range(1, 11):
            clubs.append(Card(val, self.nums[val - 1], "clubs"))
        clubs.append(Card(10, "jack", "clubs"))
        clubs.append(Card(10, "queen", "clubs"))
        clubs.append(Card(10, "king", "clubs"))
        self.deck += clubs
        return clubs


class Card:
    def __init__(self, value, name, suit):
        if not type(value) == int:
            raise TypeError("Value of card needs to be an integer")
            return
        if not suit.lower() in ["spades", "clubs", "hearts", "diamonds"]:
            raise ValueError(
                f"{suit} is not valid must be one of spades, hearts, clubs, or diamonds"
            )
        if value > 10:
            raise ValueError("Value of card cannot be greater than 10")
        self.val = value
        self.name = name.title()
        self.suit = suit.title()
        self.__create_card()

    def __create_card(self):
        self.card = {"value": self.val, "name": self.name, "suit": self.suit}
        return self.card

    def __repr__(self):
        return f"{self.card}"

    def __str__(self):
        return f"{self.name.title()} of {self.suit.title()}"
