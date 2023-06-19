"""input and output operations"""
from lib.models import Cell, Ship


def read_commands() -> list[list[str]]:
    """parse the input file"""
    with open("commands.txt", encoding="UTF-8") as reader:
        parts: list[str]

        return [
            parts
            for line in reader
            if (parts := line.strip().split())
            if parts[0].upper() in ("PLACE_SHIP", "FIRE")
        ]


def _count_remaining_ships(ships: dict[int, Ship]) -> int:
    """determine the number of ships still in play"""
    return len([ship for ship in ships.values() if not ship.is_sunk])


def get_shots(input_tokens: list[list[str]]) -> list[Cell]:
    """collect all tokens with a FIRE label"""
    return [
        Cell(token[1])
        for token in input_tokens
        if token[0].upper() == "FIRE"
    ]


def display_ship_inventory(ships: dict[int, Ship]) -> None:
    """list all the ships that were placed"""
    for ship in ships.values():
        print(f"...Placed {ship.kind}")


def _report_hit(attempt, result, ships):
    """report whether the attempt is successful"""
    print(f"++ {result.kind} hit at {attempt.location}!")
    if result.is_sunk:
        print(f"++ {result.kind} sunk at {attempt.location}!")
        print(f"++ {_count_remaining_ships(ships)} ships remain!")
