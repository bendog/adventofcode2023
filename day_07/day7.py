from collections import namedtuple

Camel = namedtuple("Camel", "hand bid")


def get_camels(raw_data: list[str]) -> list[Camel]:
    return [Camel(*x.split()) for x in raw_data]


def score_hand(hand: str) -> int:
    """find a score of the hand"""
    score = (score_type(hand) * 10000000000) + score_cards(hand)
    return score


def score_cards(hand: str) -> int:
    # get a score for the cards in the hand
    # for each card in the hand, give it a value and multpy it by an amount to make it unique
    score: int = 0
    card_rank = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    for idx, card in enumerate(hand):
        multiplier = int(100000000 / ((100**idx) if idx else 1))
        card_points = card_rank.index(card)
        score += card_points * multiplier
    return score


def score_type(hand: str) -> int:
    # get a score for the type of hand
    # count how many repeating cards are in each hand
    count = {x: hand.count(x) for x in list(set(hand))}
    matches = sorted(count.values(), reverse=True)
    if matches == [5]:
        # five of a kind
        score = 6
    elif matches == [4, 1]:
        # four of a kind
        score = 5
    elif matches == [3, 2]:
        # full house
        score = 4
    elif matches[0] == 3:
        # three of a kind
        score = 3
    elif matches[1] == 2:
        # two paid
        score = 2
    elif matches[0] == 2:
        # one pair
        score = 1
    else:
        # high card
        score = 0
    return score


def part_1(raw_data: list[str]) -> int:
    camels = get_camels(raw_data)
    print(camels)
    # for camel in camels:
    #     score_hand(camel.hand)
    camels.sort(key=lambda x: score_hand(x.hand))
    scores: list[int] = []
    for idx, camel in enumerate(camels):
        winning = (idx + 1) * int(camel.bid)
        scores.append(winning)

    return sum(scores)


def part_2(raw_data: list[str]) -> int:
    pass


def get_raw_data(path: str) -> list[str]:
    """fetch raw data from file"""
    with open(path) as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    print(part_1(get_raw_data("./input.txt")))
    print(part_2(get_raw_data("./input.txt")))
