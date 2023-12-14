from .. import day9


TEST_DATA = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45",
]


def test_day9_part1():
    assert day9.part_1(TEST_DATA) == 114


def test_day9_get_next_number():
    assert day9.get_next_number([0, 3, 6, 9, 12, 15]) == 18
    assert day9.get_next_number([1, 3, 6, 10, 15, 21]) == 28
    assert day9.get_next_number([10, 13, 16, 21, 30, 45]) == 68


# def test_day9_part2():
#     assert day9.part_2(TEST_DATA) == 6
