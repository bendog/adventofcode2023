from .. import day4

TEST_DATA = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]

WINNING_RESULT = [
    [48, 83, 86, 17],
    [32, 61],
    [1, 21],
    [84],
    [],
    [],
]

TEST_RESULT = [8, 2, 2, 1, 0, 0]


def test_day4_part1_card_winners():
    for idx, line in enumerate(TEST_DATA):
        card = day4.parse_line(line)
        win_nums = WINNING_RESULT[idx]
        card_win_nums = card.winners()
        assert all(item in win_nums for item in card_win_nums) is True


def test_day4_part1_card_score():
    for idx, line in enumerate(TEST_DATA):
        card = day4.parse_line(line)
        score = TEST_RESULT[idx]
        card_score = card.score()
        assert card_score == score


def test_day4_part1():
    assert day4.part_1(TEST_DATA) == 13
