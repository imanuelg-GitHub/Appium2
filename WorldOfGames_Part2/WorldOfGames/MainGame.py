from Live import load_game, welcome


class WorldOfGames:
    print("Please enter your name :")
    user_name = input()
    print(welcome(user_name))
    load_game()
