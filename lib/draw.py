"""functions related to showing a map of the battlefield"""
from lib.models import LETTERS_TO_INTS, Cell, Ship


_ACROSS: list[str] = [str(n) for n in LETTERS_TO_INTS.values()]
_DOWN: list[str] = list(LETTERS_TO_INTS.keys())


def generate_map(board: dict[Cell, int], ships: dict[int, Ship], hits: list[Cell]) -> None:
    """generate a map of the battlefield"""
    print("  =Game Map=")
    print(" ", "".join(n if n != "10" else "0" for n in _ACROSS))
    for alpha in _DOWN:
        print(alpha + " ", end="")
        for number in _ACROSS:
            cell: Cell = Cell(alpha + number)
            ship_key: int = board.get(cell, -1)
            kind: str = ships[ship_key].kind[0].lower() if ship_key in ships else "-"
            hit: str = "+" if cell in hits else ""
            char: str = hit if hit else kind
            print(char, end="")
        print()
