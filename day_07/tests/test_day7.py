from .. import day7

TEST_DATA = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]


def test_day7_part1():
    assert day7.part_1(TEST_DATA) == 6440


def test_day7_part2():
    assert day7.part_2(TEST_DATA) == 5905
