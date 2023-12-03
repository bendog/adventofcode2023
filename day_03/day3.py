from collections import namedtuple
from dataclasses import dataclass


def get_raw_data(path: str) -> list[str]:
    with open(path) as f:
        return [x.strip() for x in f.readlines()]


Coordinate = namedtuple("Coordinate", "col row")


@dataclass
class Cell:
    coordinates: Coordinate
    value: str | None

    @property
    def is_number(self):
        if self.value:
            return self.value.isdigit()
        return False

    @property
    def is_symbol(self):
        if self.value:
            if not self.value.isdigit() and not self.value.isalpha():
                return True
        return False


@dataclass
class Row:
    cells: list[Cell]


@dataclass
class Grid:
    rows: list[Row]

    @property
    def max_row(self):
        return len(self.rows) - 1

    @property
    def max_col(self):
        return len(self.rows[0].cells) - 1

    def check_grid_for_symbol(self, start: Coordinate, end: Coordinate) -> bool:
        """look in a grid for symbols nearby"""
        start_x, start_y = start
        start_x = start_x if start_x > 0 else 0
        start_y = start_y if start_y > 0 else 0
        end_x, end_y = end
        end_x = end_x if end_x < self.max_col else self.max_col
        end_y = end_y if end_y < self.max_row else self.max_row
        for idx_x in range(start_x, end_x + 1):
            for idx_y in range(start_y, end_y + 1):
                cell = self.rows[idx_y].cells[idx_x]
                if cell.is_symbol:
                    return True
        return False


@dataclass
class Number:
    value: int
    cells: list[Cell]

    @property
    def start(self) -> Coordinate:
        return self.cells[0].coordinates

    @property
    def end(self) -> Coordinate:
        return self.cells[-1].coordinates


def build_grid(data: list[str]) -> Grid:
    new_grid = []
    for idx_y, line in enumerate(data):
        if line.strip():
            new_row = []
            for idx_x, value in enumerate(line.strip()):
                cell = Cell((idx_x, idx_y), value if value != "." else None)
                new_row.append(cell)
            new_grid.append(Row(new_row))
    return Grid(new_grid)


def find_numbers(grid: Grid) -> list[Number]:
    numbers: list[Number] = []
    current_number: Number | None = None
    for row in grid.rows:
        if current_number:
            numbers.append(current_number)
            current_number = None
        last_cell = None
        for cell in row.cells:
            if cell.is_number:
                if not current_number:
                    # if found a new number, start a new number for processing
                    current_number = Number(int(cell.value), [cell])
                else:
                    # if not a new number, then continue to add to the previous number
                    current_number.value = int(str(current_number.value) + cell.value)
                    current_number.cells.append(cell)
            else:
                if current_number:
                    numbers.append(current_number)
                    current_number = None

    return numbers


def filter_for_numbers_with_symbols_near(grid: Grid, numbers: list[Number]) -> list[Number]:
    filtered_numbers: list[Number] = []
    for n in numbers:
        start_x, start_y = n.start
        end_x, end_y = n.end

        start = Coordinate(
            start_x - 1,
            start_y - 1,
        )

        end = Coordinate(
            end_x + 1,
            end_y + 1,
        )
        if grid.check_grid_for_symbol(start, end):
            filtered_numbers.append(n)
    return filtered_numbers


def part_1(data: list[str]) -> int:
    """solve for part 1"""
    grid = build_grid(data)
    numbers = find_numbers(grid)
    print(numbers)
    valid_numbers = filter_for_numbers_with_symbols_near(grid, numbers)
    for x in valid_numbers:
        print(x)
    return sum([n.value for n in valid_numbers])


if __name__ == "__main__":
    print(part_1(get_raw_data("./input.txt")))
