from dataclasses import dataclass


def get_raw_data(path: str) -> list[str]:
    with open(path) as f:
        return [x.strip() for x in f.readlines()]


@dataclass
class Hand:
    red: int
    green: int
    blue: int


@dataclass
class Game:
    game_id: int
    hands: list[Hand]


def parse_line(string: str) -> Game:
    game_id, raw_hands = string.split(":")
    game_id = int(game_id.replace("Game ", "").strip())
    game = Game(game_id, [])
    # get hands
    for raw_hand in raw_hands.strip().split(";"):
        hand = Hand(0, 0, 0)
        for raw_dice in raw_hand.strip().split(","):
            count, colour = raw_dice.strip().split(" ")
            setattr(hand, colour, int(count))
        game.hands.append(hand)
    return game


def check_game_under_max(game, maximums):
    for max_colour, max_value in maximums.items():
        for hand in game.hands:
            if getattr(hand, max_colour) > max_value:
                return False
    return True


def filter_valid_max(games_list: list[Game], maximums: dict = None):
    maximums = maximums or {}
    return [g for g in games_list if check_game_under_max(g, maximums)]


def part_1(data: list[str]) -> int:
    """part one
    The Elf would first like to know which games would have been possible
    if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
    """
    red_max = 12
    green_max = 13
    blue_max = 14

    games = []
    for line in data:
        games.append(parse_line(line))

    filter_games = filter_valid_max(
        games, maximums={"red": red_max, "green": green_max, "blue": blue_max}
    )

    return sum([g.game_id for g in filter_games])


if __name__ == "__main__":
    raw_data = get_raw_data("./day2input.txt")
    print(part_1(raw_data))
