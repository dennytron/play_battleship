"""input and output operations"""
from lib.hit import _count_remaining_ships
from lib.models import Ship


def read_text() -> list[list[str]]:
    """parse the input file"""
    with open("example_in.txt", encoding="UTF-8") as reader:
        return [
            line.strip().split()
            for line in reader
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
