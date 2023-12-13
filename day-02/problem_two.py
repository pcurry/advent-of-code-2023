

TEST_GAME = "Game 96: 9 blue, 12 green; 6 green, 9 blue, 11 red; 7 blue, 5 green, 10 red"


def get_draws(game):
    _, draw_block = game.split(':')
    draws = draw_block.split(';')
    return draws


def update_minimums(draw, minimum_blocks):
    color_list = draw.split(',')
    for color in color_list:
        block_count, block_color = color.strip().split()
        block_count = int(block_count)
        if block_count > minimum_blocks[block_color]:
            minimum_blocks[block_color] = block_count


def process_game(game):
    minimum_blocks = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    draws = get_draws(game)

    for draw in draws:
        update_minimums(draw, minimum_blocks)

    return minimum_blocks["red"] * minimum_blocks["green"] * minimum_blocks["blue"]


def test_update_minimums():
    minimum_blocks = {
        "red": 0,
        "blue": 10,
        "green": 0
    }
    draw = "6 green, 9 blue, 11 red"
    update_minimums(draw, minimum_blocks)
    assert minimum_blocks["red"] == 11
    assert minimum_blocks["blue"] == 10
    assert minimum_blocks["green"] == 6


def test_test_game():
    draws = get_draws(TEST_GAME)
    assert len(draws) == 3
    minimum_blocks = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    update_minimums(draws[0], minimum_blocks)
    assert minimum_blocks["red"] == 0
    assert minimum_blocks["blue"] == 9
    assert minimum_blocks["green"] == 12

    update_minimums(draws[1], minimum_blocks)
    assert minimum_blocks["red"] == 11
    assert minimum_blocks["blue"] == 9
    assert minimum_blocks["green"] == 12

    update_minimums(draws[2], minimum_blocks)
    assert minimum_blocks["red"] == 11
    assert minimum_blocks["blue"] == 9
    assert minimum_blocks["green"] == 12

    power = process_game(TEST_GAME)
    assert power == (11 * 9 * 12)
    

if __name__ == "__main__":
    game_data_filename = "game_data.txt"

    test_update_minimums()
    test_test_game()

    with open(game_data_filename, "r") as fin:
        game_data_lines = fin.readlines()

    game_powers = [
        process_game(game) for game in game_data_lines
    ]

    print(sum(game_powers))
    
