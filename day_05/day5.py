import datetime
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class Seed:
    id: int
    soil: int = None
    fertilizer: int = None
    water: int = None
    light: int = None
    temperature: int = None
    humidity: int = None
    location: int = None

    @staticmethod
    def match_value(from_val: int, from_start: int, to_start: int) -> int:
        """given these have already matched, return the to_value to match the from_value difference"""
        return to_start + (from_val - from_start)

    def process_maps(self, map_from: str, map_to: str, values: list[list[int]]):
        """process the map selection for this seed"""
        from_value: int
        to_value: int
        # Get the from value to check against
        if map_from == "seed":
            from_value = self.id
        else:
            from_value = getattr(self, map_from)
        # set the default to value
        to_value = from_value

        for to_start, from_start, length in values:
            if from_start <= from_value <= from_start + length:
                to_value = self.match_value(from_value, from_start, to_start)
                break
        setattr(self, map_to, to_value)


Sections = dict[str, list[int | list[int]]]


def split_sections(data: list[str]) -> Sections:
    segments = defaultdict(list)
    title: str | None = None
    for line in data:
        if not line.strip():
            title = None
        elif ":" in line.strip():
            if line.find(":") + 1 != len(line.strip()):
                # if this is a value set where the values are on the same line
                title, values = line.strip().split(":")
                segments[title] = [int(x.strip()) for x in values.strip().split()]
            else:
                title = line.replace(" map:", "").strip()
        else:
            segments[title].append([int(x.strip()) for x in line.strip().split()])
    return segments


def process_seeds(sections: Sections) -> list[Seed]:
    return [Seed(x) for x in sections["seeds"]]


def process_maps(seeds: list[Seed], sections: Sections):
    for section_title, value_list in sections.items():
        if "-to-" in section_title:
            map_from, map_to = section_title.strip().split("-to-")
            for seed in seeds:
                seed.process_maps(map_from, map_to, value_list)
    pass


def part_1(raw_data: list[str]) -> int:
    sections = split_sections(raw_data)
    seeds: list[Seed] = process_seeds(sections)
    process_maps(seeds, sections)
    return min([x.location for x in seeds])


###
# PART TWO NEEDS A REWRITE
###


def process_seeds_part2(sections: Sections) -> list[Seed]:
    seeds = []
    iter_seeds = iter(sections["seeds"])
    seed_pairs = list(zip(iter_seeds, iter_seeds))
    for start, length in seed_pairs:
        for x in range(start, start + length):
            seeds.append(Seed(x))
    return seeds


def part_2(raw_data: list[str]) -> int:
    start = datetime.datetime.now().timestamp()
    sections = split_sections(raw_data)
    seeds: list[Seed] = process_seeds_part2(sections)
    print(f"seeds done - {(datetime.datetime.now().timestamp() - start):.2f} seconds")
    # len_seeds = len(seeds)
    # print(
    #     f"created {len_seeds} seeds - {(datetime.datetime.now().timestamp() - start):.2f} seconds"
    # )
    segment = datetime.datetime.now().timestamp()
    process_maps(seeds, sections)
    print(
        f"processed seeds - {(datetime.datetime.now().timestamp() - segment):.2f} / {(datetime.datetime.now().timestamp() - start):.2f} seconds"
    )
    segment = datetime.datetime.now().timestamp()
    minimum = min(x.location for x in seeds)
    print(
        f"found minimum {minimum} - {(datetime.datetime.now().timestamp() - segment):.2f} / {(datetime.datetime.now().timestamp() - start):.2f} seconds"
    )
    return minimum


def get_raw_data(path: str) -> list[str]:
    """fetch raw data from file"""
    with open(path) as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    print(part_1(get_raw_data("./input.txt")))
    print(part_2(get_raw_data("./input.txt")))
