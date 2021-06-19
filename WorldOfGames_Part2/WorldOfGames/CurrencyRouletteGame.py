from typing import Final
from Utilities import validate_input, generate_random_number, get_user_input, get_fx_rate

LEVEL: Final = 5
MIN: Final = 1
MAX: Final = 100


class CurrencyRouletteGame:

    # get the exchange rate between 2 currencies and calculate money interval
    def get_money_interval(self, game_difficulty):
        fx_rate = get_fx_rate()
        amount = generate_random_number(MIN, MAX)
        # random amount, ccy1, ccy2, first interval, second interval, amount in ccy2
        # round to 2 decimals for comfort
        return round(amount, 2), \
               fx_rate[0], \
               fx_rate[1], \
               round(amount * fx_rate[2] - (LEVEL - int(game_difficulty)), 2), \
               round(amount * fx_rate[2] + (LEVEL - int(game_difficulty)), 2), \
               round(amount * fx_rate[2], 2)

    def compare_results(self, game_difficulty):
        output = self.get_money_interval(game_difficulty)
        print("\nPlease guess how much", output[0], output[1].upper(), "is in", output[2].upper())
        user_input = get_user_input(1, MIN - 1, None)  # only 1 item in user_list in this game, min is 0
        try:
            validate_input(user_input[0], output[3], output[4])
        except ValueError:
            return False, output
        else:
            return True, output

    def play(self, game_difficulty):
        print("Playing : CurrencyRouletteGame...")
        out = self.compare_results(game_difficulty)
        if out[0]:
            print("You rightly guessed. You won !!!")
        else:
            print("Sorry but you lost")
        print(out[1][0], out[1][1].upper(), "is", out[1][5], out[1][2].upper())
