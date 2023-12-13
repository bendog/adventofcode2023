from .. import day6

TEST_DATA = [
    "Time:      7  15   30",
    "Distance:  9  40  200",
]


def test_day6_part1():
    assert day6.part_1(TEST_DATA) == 288


def test_get_distance():
    assert day6.get_distance(0, 7) == 0
    assert day6.get_distance(1, 7) == 6
    assert day6.get_distance(2, 7) == 10
    assert day6.get_distance(3, 7) == 12
    assert day6.get_distance(4, 7) == 12
    assert day6.get_distance(5, 7) == 10
    assert day6.get_distance(6, 7) == 6
    assert day6.get_distance(7, 7) == 0


def test_filter_distances():
    assert day6.filter_distances(7, 9) == [10, 12, 12, 10]


def test_day6_part2():
    assert day6.part_2(TEST_DATA) == 71503
