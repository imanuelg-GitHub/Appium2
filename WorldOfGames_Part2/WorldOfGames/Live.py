# even though it looks like these imports are unused (greyed out), they are in run time !!
from MemoryGame import MemoryGame
from GuessGame import GuessGame
from CurrencyRouletteGame import CurrencyRouletteGame
import os
from Utilities import validate_input
from typing import Final
import sys

# define consts only for this file
MIN: Final = 1
MAX: Final = 4
MAX_DIFFICULTY: Final = 5


def welcome(name):
    welcome_str = "Hello " + name + " and welcome to the World of Games (WoG).\nHere you can find many cool games to " \
                                    "play.\n\n "
    return welcome_str


def convert_str_to_class(str):
    return getattr(sys.modules[__name__], str)


def load_game():
    games_dictionary = {
        "1": "MemoryGame",
        "2": "GuessGame",
        "3": "CurrencyRouletteGame"
    }

    while True:
        print("\n\nPlease choose a game to play:")
        print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
        print("2. Guess Game - guess a number and see if you chose like the computer")
        print("3. Currency Roulette - try and guess the value of a random amount between 2 currencies")
        print("4. Quit\n\n")

        game_number = input()
        try:
            validate_input(int(game_number), MIN, MAX)
        except ValueError:
            print("\nYou made an invalid menu selection\nPlease try again...")
        else:
            if int(game_number) == MAX:
                break
            while True:
                print("\n\nPlease choose game difficulty from", MIN, "to", MAX_DIFFICULTY, ": ")
                game_difficulty = input()
                try:
                    validate_input(int(game_difficulty), MIN, MAX_DIFFICULTY)
                except ValueError:
                    print("\nYou made an invalid game difficulty selection\nPlease try again...")
                else:
                    print(
                        "\n\nYou selected game number : " + game_number + " and game difficulty : " + game_difficulty + "\n\n")

                    # polymorphism to override the play() method for each game
                    # refer to the implementation of each play() method in each game's class
                    # we call the 'correct' play() method depending on game selection from games_dictionary
                    convert_str_to_class(games_dictionary[game_number])().play(int(game_difficulty))

                    answer = input("\n\n\nPlay again this game ('N' - Back to main menu) ? ")
                    if answer == 'N':
                        break

                    os.system('cls')
