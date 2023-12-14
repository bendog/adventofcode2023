from collections import namedtuple

Paths = namedtuple("Paths", "left right")


def parse_file(raw_data: list[str]) -> tuple[str, dict[str, Paths]]:
    pattern = raw_data[0].strip()
    paths = {}
    for line in raw_data[2:]:
        key, path_pair = line.strip().split(" = ")
        paths[key] = Paths(
            *[x.strip() for x in path_pair.replace("(", "").replace(")", "").split(", ")]
        )
    return pattern, paths


def pattern_generator(pattern: str) -> int:
    idx = -1
    while True:
        if idx >= len(pattern) - 1:
            idx = 0
        else:
            idx += 1
        if pattern[idx] not in ["L", "R"]:
            raise ValueError("Invalid Pattern")
        yield 0 if pattern[idx] == "L" else 1


def pattern_walk(pattern: str, paths: dict[str, Paths]) -> int:
    steps = 0
    current_node = "AAA"
    for step in pattern_generator(pattern):
        new_node = paths[current_node][step]
        steps += 1
        if new_node == "ZZZ":
            break
        if new_node == current_node:
            raise NotImplementedError("Dead End")
        current_node = new_node
    return steps


def part_1(raw_data: list[str]) -> int:
    pattern, paths = parse_file(raw_data)
    return pattern_walk(pattern, paths)


def part_2(raw_data: list[str]) -> int:
    pass


def get_raw_data(path: str) -> list[str]:
    """fetch raw data from file"""
    with open(path) as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    print(part_1(get_raw_data("./input.txt")))
    print(part_2(get_raw_data("./input.txt")))
