def get_next_number(series: list[int], reverse=False) -> int:
    differences = []
    for idx, x in enumerate(series):
        if idx < len(series) - 1:
            differences.append(series[idx + 1] - x)
    if set(differences) == {0}:
        return series[-1]
    else:
        if reverse:
            return series[0] - get_next_number(differences, reverse=reverse)
        return get_next_number(differences, reverse=reverse) + series[-1]


def parse_input(raw_data: list[str]) -> list[list[int]]:
    data: list[list[int]] = []
    for line in raw_data:
        data.append([int(x.strip()) for x in line.strip().split()])
    return data


def part_1(raw_data: list[str]) -> int:
    next_numbers = []
    for item in parse_input(raw_data):
        next_numbers.append(get_next_number(item))
    return sum(next_numbers)


def part_2(raw_data: list[str]) -> int:
    next_numbers = []
    for item in parse_input(raw_data):
        next_numbers.append(get_next_number(item, reverse=True))
    return sum(next_numbers)


def get_raw_data(path: str) -> list[str]:
    """fetch raw data from file"""
    with open(path) as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    print(part_1(get_raw_data("./input.txt")))
    print(part_2(get_raw_data("./input.txt")))
