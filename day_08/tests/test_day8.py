from .. import day8

TEST_DATA = [
    "RL",
    "",
    "AAA = (BBB, CCC)",
    "BBB = (DDD, EEE)",
    "CCC = (ZZZ, GGG)",
    "DDD = (DDD, DDD)",
    "EEE = (EEE, EEE)",
    "GGG = (GGG, GGG)",
    "ZZZ = (ZZZ, ZZZ)",
]

TEST_DATA_2 = [
    "LLR",
    "",
    "AAA = (BBB, BBB)",
    "BBB = (AAA, ZZZ)",
    "ZZZ = (ZZZ, ZZZ)",
]


def test_day8_part1():
    assert day8.part_1(TEST_DATA) == 2
    assert day8.part_1(TEST_DATA_2) == 6


# def test_day8_part2():
#     assert day8.part_2(TEST_DATA) == 5905
