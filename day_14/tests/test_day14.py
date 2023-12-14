from .. import day14

TEST_DATA = [
    "O....#....",
    "O.OO#....#",
    ".....##...",
    "OO.#O....O",
    ".O.....O#.",
    "O.#..O.#.#",
    "..O..#O..O",
    ".......O..",
    "#....###..",
    "#OO..#....",
]


def test_day14_part1():
    assert day14.part_1(TEST_DATA) == 136


def test_grid_north():
    start_grid = [
        list("O....#...."),
        list("O.OO#....#"),
        list(".....##..."),
        list("OO.#O....O"),
        list(".O.....O#."),
        list("O.#..O.#.#"),
        list("..O..#O..O"),
        list(".......O.."),
        list("#....###.."),
        list("#OO..#...."),
    ]
    end_grid = [
        list("OOOO.#.O.."),
        list("OO..#....#"),
        list("OO..O##..O"),
        list("O..#.OO..."),
        list("........#."),
        list("..#....#.#"),
        list("..O..#.O.O"),
        list("..O......."),
        list("#....###.."),
        list("#....#...."),
    ]
    day14.tilt_grid(start_grid, day14.XYPair(0, -1))
    assert start_grid == end_grid
