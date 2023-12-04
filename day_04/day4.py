from dataclasses import dataclass


def get_raw_data(path: str) -> list[str]:
    with open(path) as f:
        return [x.strip() for x in f.readlines()]


@dataclass
class Card:
    card_id: int
    winning_numbers: list[int]
    numbers: list[int]

    def winners(self) -> list[int]:
        return [x for x in self.numbers if x in self.winning_numbers]

    def score(self) -> int:
        """scores are based on num of winners
        [0, 1, 2, 4, 8, 16, 32]
        """
        if len(self.winners()):
            if len(self.winners()) <= 2:
                return len(self.winners())
            else:
                return 2 ** (len(self.winners()) - 1)
        return 0


def parse_line(line: str) -> Card:
    card_id, wins, nums = line.strip().replace(":", "|").split("|")
    x, card_id_num = card_id.strip().split()
    win_nums = [int(x) for x in wins.replace("  ", " ").strip().split()]
    num_nums = [int(x) for x in nums.replace("  ", " ").strip().split()]
    return Card(card_id_num, win_nums, num_nums)


def part_1(data: list[str]) -> int:
    """solve for part 1"""
    cards: list[Card] = [parse_line(line) for line in data if line.strip()]
    print(cards)
    return sum([x.score() for x in cards])


if __name__ == "__main__":
    print(part_1(get_raw_data("./input.txt")))
