"""input and output operations"""
import sys
from pathlib import Path

from lib.models import Cell, Ship


def read_commands(commands_file: Path) -> list[list[str]]:
    """parse the input file"""
    if not commands_file.exists():
        print(f"Warning: commands file not found at {commands_file.absolute()}")
        sys.exit(1)

    with open(commands_file, encoding="UTF-8") as reader:
        commands: list[list[str]] = [
            parts
            for line in reader
            if (parts := line.strip().split())
            if parts[0].upper() in ("PLACE_SHIP", "FIRE")
        ]

        if not commands:
            print("Please provide a valid list of commands in your commands file")
            print("PLACE_SHIP and FIRE are the valid commands")
            sys.exit(1)

        return commands


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


def display_ship_inventory(ships: dict[int, Ship], board: dict[Cell, int]) -> None:
    """list all the ships that were placed"""
    for ship_key in set(board.values()):
        ship: Ship = ships[ship_key]
        print(f"...Placed {ship.kind}")


def _report_hit(attempt: Cell, result: Ship, ships: dict[int: Ship]) -> None:
    """report whether the attempt is successful"""
    print(f"++ {result.kind} hit at {attempt.location}!")
    if result.is_sunk:
        print(f"++ {result.kind} sunk at {attempt.location}!")
        print(f"++ {_count_remaining_ships(ships)} ships remain!")
