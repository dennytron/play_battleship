"""data models for the application"""
from dataclasses import dataclass


@dataclass
class Ship:
    """contains the data representing a ship"""
    key: int
    size: int
    direction: str
    start: str
    kind: str
    hits: int = 0

    @property
    def is_sunk(self) -> bool:
        """determine whether this ship is sunk"""
        return self.hits == self.size


@dataclass(frozen=True, eq=True)
class Cell:
    """represents one cell on the board"""
    location: str

    @property
    def x_value(self) -> int:
        """returns the x value"""
        return int(self.location[1:])

    @property
    def y_value(self) -> str:
        """returns the y value"""
        return self.location[0]

    @property
    def y_as_int(self) -> int:
        """returns the y value mapped to an integer"""
        if self.location[0] not in LETTERS_TO_INTS:
            raise NotImplementedError(f"Letter not supported {self.location[0]}")
        return LETTERS_TO_INTS[self.location[0]]


SHIP_TYPES: dict[str, int] = {
    "carrier": 5,
    "battleship": 4,
    "cruiser": 3,
    "submarine": 3,
    "destroyer": 2
}

LETTERS_TO_INTS: dict[str, int] = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10
}

INTS_TO_LETTERS: dict[int, str] = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "J"
}
