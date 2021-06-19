import os
import time
from typing import Final
from Utilities import generate_random_number, get_user_input

# define consts only for this file
MIN: Final = 1
MAX: Final = 101
interval: Final = 0.7


class MemoryGame:

    def generate_sequence(self, game_difficulty):
        random_list = []
        for i in range(0, int(game_difficulty)):
            random_list.append(generate_random_number(MIN, MAX))

        print(random_list)
        time.sleep(interval * len(random_list))
        os.system('cls')  # this is working on Windows
        return random_list

    def is_list_equal(self, game_difficulty):
        random_list = self.generate_sequence(game_difficulty)
        user_list = get_user_input(game_difficulty, MIN, MAX)
        if random_list == user_list:
            return True, random_list
        return False, random_list, user_list

    def play(self, game_difficulty):
        print("Playing : MemoryGame...")
        output = self.is_list_equal(game_difficulty)
        if output[0]:
            print("You rightly guessed", output[1], "You won !!!")
        else:  # we are returning list of floats, nicer to convert to int
            print("Sorry but you lost, the random list was :", output[1], "but you guessed :", ([int(i) for i in output[2]]))
