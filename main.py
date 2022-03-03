from utils import clear, cprint, colors
from blackjack import Game

def main():
    game = Game()
    game.get_player_name()
    game.start_game()
main()