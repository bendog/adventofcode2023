from collections import namedtuple

ROUND_ROCK = "O"
CUBE_ROCK = "#"
DUST = "."

RawData = list[str]
Grid = list[list[str]]

XYPair = namedtuple("Direction", "x y")


def build_grid(raw_data: RawData) -> Grid:
    return [list(x.strip()) for x in raw_data]


def tilt_cell(grid: Grid, coords: XYPair, direction: XYPair):
    if grid[coords.y][coords.x] == ROUND_ROCK:
        check = XYPair(coords.x + direction.x, coords.y + direction.y)
        if 0 <= check.y < len(grid) and 0 <= check.x < len(grid[0]):
            check_cell = grid[check.y][check.x]
            if check_cell == DUST:
                grid[check.y][check.x] = ROUND_ROCK
                grid[coords.y][coords.x] = DUST
                tilt_cell(grid, check, direction)
    return


def tilt_grid(grid: Grid, direction: XYPair):
    """I tried to make this generic, but since it's top down, it will only work for tilting north"""
    for idy, row in enumerate(grid):
        for idx, cell in enumerate(row):
            tilt_cell(grid, XYPair(idx, idy), direction)

    pass


def part_1(raw_data: RawData) -> int:
    grid = build_grid(raw_data)
    tilt_grid(grid, XYPair(0, -1))
    num_rows = len(grid)
    for x in grid:
        print("".join(x))
    loads = [row.count(ROUND_ROCK) * (num_rows - idx) for idx, row in enumerate(grid)]

    return sum(loads)


def part_2(raw_data: RawData) -> int:
    pass


def get_raw_data(path: str) -> RawData:
    """fetch raw data from file"""
    with open(path) as f:
        return [x.strip() for x in f.readlines()]


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


if __name__ == "__main__":
    print(part_1(TEST_DATA))
    print(part_1(get_raw_data("./input.txt")))
    print(part_2(get_raw_data("./input.txt")))
