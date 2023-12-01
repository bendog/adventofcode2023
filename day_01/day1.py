import re
from collections import defaultdict

import polars as pl


def get_raw_data(path: str) -> list[str]:
    with open(path) as f:
        return [x.strip() for x in f.readlines()]


def strip_non_numeric(s: str) -> str:
    return "".join(x for x in s if x.isnumeric())


def part_1(data: list[str]) -> int:
    processed_data = [strip_non_numeric(x) for x in data]
    # numbers = [int(x[0] + x[-1]) if len(x) > 1 else int(x) for x in processed_data]
    numbers = [int(x[0] + x[-1]) for x in processed_data]
    return sum(numbers)


def convert_word_to_num(s: str) -> str:
    conversions = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    print(s)

    def find_words(ss: str) -> dict[str, list[int]]:
        found = {}
        for k, v in conversions.items():
            found[k] = list(found.start() for found in re.finditer(k, s) if found)
            # idx = s.find_all(k)
            # if idx >= 0:
            #     found[k].append(idx)
            #     # print(f"{k} found at {s.find(k)}")
        return found

    index = find_words(s)
    # # get the first number
    # first_idx = min(index.values())
    # first_key = [k for k, v in index.items() if v == first_idx][0]
    # s = s.replace(first_key, str(conversions[first_key]))
    #
    # # get the last number
    # index = find_words(s)
    # if index:
    #     last_idx = max(index.values())
    #     last_key = [k for k, v in index.items() if v == last_idx][-1]
    #     s = s.replace(last_key, str(conversions[last_key]))

    # it seems that it needs to be not the first and last, but process the whole line in order.
    # sorted_index = sorted(index.items(), key=lambda x: x[1])
    # print(sorted_index)
    # for k, v in sorted_index:
    #     s = s.replace(k, str(conversions[k]))
    # print(s)

    # perhaps all of the words need to be replaced with numbers in the position they are?
    list_s = list(s)
    for k, v in index.items():
        for idx in v:
            list_s[idx] = str(conversions[k])
    return "".join(list_s)


def part_2(data: list[str]) -> int:
    processed_data = [convert_word_to_num(x) for x in data]
    processed_data = [strip_non_numeric(x) for x in processed_data]
    numbers = [int(x[0] + x[-1]) for x in processed_data]
    # numbers = [int(x[0] + x[-1]) if len(x) > 1 else int(x) for x in processed_data]
    return sum(numbers)


if __name__ == "__main__":
    print(part_1(get_raw_data("./day1input.txt")))
    print(part_2(get_raw_data("./day1input.txt")))
