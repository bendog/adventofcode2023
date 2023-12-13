from collections import namedtuple
from functools import reduce
from operator import mul


def get_distance(hold_time: int, race_time: int) -> float:
    return hold_time * (race_time - hold_time)


def filter_distances(race_time: int, check_distance: int) -> list[float]:
    return [
        get_distance(x, race_time)
        for x in range(1, race_time)
        if get_distance(x, race_time) > check_distance
    ]


Race = namedtuple("Race", "time distance")


def get_races(raw_data: list[str]) -> list[Race]:
    time, distance = raw_data[0:2]
    times = [int(val.strip()) for val in time.split(":")[1].split() if val]
    distances = [int(val.strip()) for val in distance.split(":")[1].split() if val]
    return [Race(t, d) for t, d in zip(times, distances)]


def part_1(raw_data: list[str]) -> int:
    races = get_races(raw_data)
    valid_races = [filter_distances(*x) for x in races]
    return reduce(mul, (len(x) for x in valid_races))


def get_race(raw_data: list[str]) -> Race:
    time, distance = raw_data[0:2]
    time = int(time.replace("Time:", "").replace(" ", ""))
    distance = int(distance.replace("Distance:", "").replace(" ", ""))
    return Race(time, distance)
    pass


def part_2(raw_data: list[str]) -> int:
    """BRUTE FORCE JERKS AGAIN"""
    race = get_race(raw_data)
    hold_time: int = 0
    for hold_time in range(1, race.time):
        if get_distance(hold_time, race.time) > race.distance:
            break
    return race.time - (hold_time * 2) + 1
    pass


def get_raw_data(path: str) -> list[str]:
    """fetch raw data from file"""
    with open(path) as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    print(part_1(get_raw_data("./input.txt")))
    print(part_2(get_raw_data("./input.txt")))
