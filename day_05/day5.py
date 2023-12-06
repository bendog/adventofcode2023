from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class Seed:
    id: int
    soil_set: set[int] = field(default_factory=set)
    fertilizer_set: set[int] = field(default_factory=set)
    water_set: set[int] = field(default_factory=set)
    light_set: set[int] = field(default_factory=set)
    temperature_set: set[int] = field(default_factory=set)
    humidity_set: set[int] = field(default_factory=set)
    location_set: set[int] = field(default_factory=set)

    def process_range(self, from_str, to_str, from_values, to_values):
        if from_str == "seed":
            if self.id not in from_values:
                return
            else:
                getattr(self, f"{to_str}_set").update(to_values)
        else:
            if getattr(self, f"{from_str}_set").intersection(set(from_values)):
                getattr(self, f"{to_str}_set").update(to_values)
        pass


Sections = dict[str, list[int]]


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
            for to_start, from_start, length in value_list:
                from_values = list(range(from_start, from_start + length))
                to_values = list(range(to_start, to_start + length))
                for seed in seeds:
                    seed.process_range(map_from, map_to, from_values, to_values)

    pass


def part_1(raw_data: list[str]) -> int:
    sections = split_sections(raw_data)
    seeds: list[Seed] = process_seeds(sections)
    process_maps(seeds, sections)
    return


def get_raw_data(path: str) -> list[str]:
    """fetch raw data from file"""
    with open(path) as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    print(part_1(get_raw_data("./input.txt")))
    # print(part_2(get_raw_data("./input.txt")))
