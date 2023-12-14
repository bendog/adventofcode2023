from collections import namedtuple

ROUND_ROCK = "O"
CUBE_ROCK = "#"
DUST = "."

RawData = list[str]
Grid = list[list[str]]

XYPair = namedtuple("Direction", "x y")
NORTH = XYPair(0, -1)
SOUTH = XYPair(0, 1)
WEST = XYPair(-1, 0)
EAST = XYPair(1, 0)


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
    if direction.y > 0:
        y_range = range(len(grid) - 1, -1, -1)
    else:
        y_range = range(len(grid))
    if direction.x > 0:
        x_range = range(len(grid[0]) - 1, -1, -1)
    else:
        x_range = range(len(grid))
    for idy in y_range:
        for idx in x_range:
            tilt_cell(grid, XYPair(idx, idy), direction)

    pass


def part_1(raw_data: RawData) -> int:
    grid = build_grid(raw_data)
    tilt_grid(grid, NORTH)
    num_rows = len(grid)
    # for x in grid:
    #     print("".join(x))
    loads = [row.count(ROUND_ROCK) * (num_rows - idx) for idx, row in enumerate(grid)]

    # print(grid)
    return sum(loads)


def part_2(raw_data: RawData) -> int:
    grid = build_grid(raw_data)
    # for cycle in range(3):
    for cycle in range(1_000):
        tilt_grid(grid, NORTH)
        tilt_grid(grid, WEST)
        tilt_grid(grid, SOUTH)
        tilt_grid(grid, EAST)
        # print("-" * 15)
        # for x in grid:
        #     print("".join(x))
    num_rows = len(grid)
    loads = [row.count(ROUND_ROCK) * (num_rows - idx) for idx, row in enumerate(grid)]
    return sum(loads)


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
    # print(part_1(TEST_DATA))
    print(part_1(get_raw_data("./input.txt")))
    # print(part_2(TEST_DATA))
    print(part_2(get_raw_data("./input.txt")))
