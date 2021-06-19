from typing import Final
from Utilities import generate_random_number, get_user_input

# define consts only for this file
# exercise says number between 1 to difficulty but if the user selects 1 then he will always win
# So we agreed in class to start from 0
MIN: Final = 0


class GuessGame:

    def compare_results(self, game_difficulty):
        secret_number = generate_random_number(MIN, game_difficulty)
        print("Guess a number between", MIN, "and", game_difficulty)
        user_list = get_user_input(1, MIN, int(game_difficulty))  # only 1 item in user_list in this game
        if secret_number == user_list[0]:
            return True, secret_number
        return False, secret_number

    def play(self, game_difficulty):
        print("Playing : GuessGame...")
        output = self.compare_results(game_difficulty)
        if output[0]:
            print("You rightly guessed", output[1], "You won !!!")
        else:
            print("Sorry but you lost, the number to guess was :", output[1])
