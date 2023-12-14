import math
from collections import namedtuple

Paths = namedtuple("Paths", "left right")


def parse_file(raw_data: list[str]) -> tuple[str, dict[str, Paths]]:
    pattern = raw_data[0].strip()
    paths = {}
    for line in raw_data[2:]:
        key, path_pair = line.strip().split(" = ")
        key = key.strip()
        if key:
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


Walk = namedtuple("Walk", "steps node")


def pattern_walk(pattern: str, paths: dict[str, Paths], start_node: str = "AAA") -> Walk:
    steps = 0
    current_node = start_node
    for step in pattern_generator(pattern):
        new_node = paths[current_node][step]
        steps += 1
        if new_node == current_node:
            raise NotImplementedError("Dead End")
        current_node = new_node
        yield Walk(steps, current_node)


def part_1(raw_data: list[str]) -> int:
    pattern, paths = parse_file(raw_data)
    for steps, current_node in pattern_walk(pattern, paths):
        if current_node[-1] == "Z":
            return steps


def part_2(raw_data: list[str]) -> int:
    pattern, paths = parse_file(raw_data)
    journeys: dict[str, Walk] = {
        pkey: pattern_walk(pattern, paths, start_node=pkey)
        for pkey, pval in paths.items()
        if pkey[-1] == "A"
    }
    # count: int = 0
    # while True:
    #     count += 1
    #     journey_stage: list[Walk] = [v.__next__() for v in journeys.values()]
    #     print(journey_stage)
    #     if len([x for x in journey_stage if x.node[-1] != "Z"]) == 0:
    #         return count
    taken_steps: list[int] = []
    for start_node, journey in journeys.items():
        for steps, current_node in pattern_walk(pattern, paths, start_node=start_node):
            if current_node[-1] == "Z":
                break
        taken_steps.append(steps)
    return math.lcm(*taken_steps)


def get_raw_data(path: str) -> list[str]:
    """fetch raw data from file"""
    with open(path) as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    print(part_1(get_raw_data("./input.txt")))
    print(part_2(get_raw_data("./input.txt")))
