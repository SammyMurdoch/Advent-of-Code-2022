def get_game_result1(letter_numerical_value, game):
    return ((letter_numerical_value[game[1]] - letter_numerical_value[game[0]] + 1) % 3) * 3


def get_game_result2(letter_numerical_value, game):
    return (letter_numerical_value[game[0]] + letter_numerical_value[game[1]]) % 3 + 1


with open("Strategy Guide") as f:
    lines = f.read()

games = [game.split(" ") for game in lines.split("\n")]

letter_numerical_value = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

game_scores1 = [letter_numerical_value[game[1]] + get_game_result1(letter_numerical_value, game) for game in games]

print(sum(game_scores1))

game_scores2 = [(letter_numerical_value[game[1]] - 1) * 3 + get_game_result2(letter_numerical_value, game) for game in games]

print(game_scores2)