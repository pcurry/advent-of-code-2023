
# import re

MAX_LOOKUP = {
    "blue": 14,
    "green":13,
    "red": 12
}
TEST_GAME = "Game 96: 9 blue, 12 green; 6 green, 9 blue, 11 red; 7 blue, 5 green, 10 red"
BAD_DRAW_BLUE = "17 blue"
BAD_DRAW_GREEN = "15 green"
BAD_DRAW_RED = "13 red"


def get_game_id(game):
    id_block, rest = game.split(':')
    _, id_number = id_block.split()
    return int(id_number)


def get_draws(game):
    _, draw_block = game.split(':')
    draws = draw_block.split(';')
    return draws


def check_a_draw(draw):
    color_list = draw.split(',')
    for color in color_list:
        block_count, block_color = color.strip().split()
        if int(block_count) > MAX_LOOKUP[block_color]:
            return False
    return True


def process_game(game):
    draws = get_draws(game)
    possible = True
    for draw in draws:
        possible = possible and check_a_draw(draw)

    if possible:
        return get_game_id(game)
    else:
        return 0


def test_check_a_draw():
    assert not check_a_draw(BAD_DRAW_BLUE)
    assert not check_a_draw(BAD_DRAW_GREEN)
    assert not check_a_draw(BAD_DRAW_RED)


def test_test_game():
    game_id = get_game_id(TEST_GAME)
    assert game_id == 96
    draws = get_draws(TEST_GAME)
    assert len(draws) == 3
    for draw in draws:
        assert check_a_draw(draw)
    process_result = process_game(TEST_GAME)
    assert process_result == game_id


if __name__ == "__main__":
    game_data_filename = "game_data.txt"

    test_check_a_draw()
    test_test_game()

    with open(game_data_filename, "r") as fin:
        game_data_lines = fin.readlines()

    possible_games = [
        process_game(game)
        for game in game_data_lines
    ]
    print(sum(possible_games))   
