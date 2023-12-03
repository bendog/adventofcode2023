from .. import day3

TEST_DATA = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


def test_part_1():
    assert day3.part_1(TEST_DATA) == 4361


def test_part_2():
    assert day3.part_2(TEST_DATA) == 467835
