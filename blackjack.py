from random import choice
from utils import colors, clear, print_header, cprint
from deck import Deck
from time import sleep

class Game:
    def __init__(self):
        self.name = "anon player"
        self.user_balance = 1000
        self.picked = []
        self.deck = Deck().deck
        self.player_cards = []
        self.dealer_cards = []
    def get_player_name(self):
        name = input(
            f"{print_header()}\n{colors.green}What is your name? {colors.end}"
        )
        clear()
        self.name = name if name != "" else "anon player"

    def start_game(self):
        print_header()
        cprint(s=f"Welcome, {self.name}. Let's play!")
        clear()
        self.collect_bets()
        self.get_first_cards()
        self.show_cards()

    def get_first_cards(self):
        cprint(color=colors.bright_green, s='Dealing Cards...\n', end=colors.end)
        user_card_1 = choice(self.deck)
        while user_card_1 in self.picked:
            user_card_1 = choice(self.deck)
        self.picked.append(user_card_1)
        user_card_2 = choice(self.deck)
        while user_card_2 in self.picked:
            user_card_2 = choice(self.deck)
        self.picked.append(user_card_2)
        dealer_card_1 = choice(self.deck)
        while dealer_card_1 in self.picked:
            dealer_card_1 = choice(self.deck)
        dealer_card_2 = choice(self.deck)
        self.picked.append(dealer_card_1)
        while dealer_card_2 in self.picked:
            dealer_card_2 = choice(self.deck)
        self.picked.append(dealer_card_2)

        self.player_cards.append(user_card_1)
        self.player_cards.append(user_card_2)
        self.dealer_cards.append(dealer_card_1)
        self.dealer_cards.append(dealer_card_2)
    def collect_bets(self):
      self.display_balance()
      user_bet = input(f'{colors.green}How much would you like to bet? ')
      print(colors.end, end='')
      try:
        self.user_bet = float(user_bet)
      except ValueError:
        cprint(color=colors.red, s='Error: Bet must be a number')
        self.collect_bets()
      cprint(color=colors.bright_green, s='Money Collected...\n', end='')
      sleep(0.5)    

    def display_balance(self):
      cprint(color=colors.bright_blue, s=f'You have ${self.user_balance}')
    def show_cards(self):
      cprint(s=f'Player Total: {self.player_cards[0].val + self.player_cards[1].val}\nFrom {self.player_cards[0]}, {self.player_cards[1]}')