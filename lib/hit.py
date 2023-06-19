"""functions related to making hits on the board"""
from lib.models import Cell, Ship


def _try_to_hit(location: Cell, board: dict[Cell, int], ships: dict[int, Ship]) -> Ship | None:
    """at the Cell location, determine if the player hit a ship on the board"""
    if location in board:
        ship_key: int = board[location]
        return ships.get(ship_key)
    return None


def _count_remaining_ships(ships: dict[int, Ship]) -> int:
    """determine the number of ships still in play"""
    return len([ship for ship in ships.values() if not ship.is_sunk])


def _report_hit(attempt, result, ships):
    """report whether the attempt is successful"""
    print(f"++ {result.kind} hit at {attempt.location}!")
    if result.is_sunk:
        print(f"++ {result.kind} sunk at {attempt.location}!")
        print(f"++ {_count_remaining_ships(ships)} ships remain!")


def attempt_hits(
        attempts: list[Cell],
        board: dict[Cell, int],
        ships: dict[int, Ship]) -> list[Cell]:
    """given attempts at Cells, try to sink ships on the board"""
    hits: list[Cell] = []
    for attempt in attempts:
        result: Ship | None = _try_to_hit(attempt, board, ships)
        miss: bool = result is None or result.is_sunk

        if miss:
            print(f"-- Miss at {attempt.location}!")
        else:
            assert result is not None
            result.hits += 1
            _report_hit(attempt, result, ships)
            hits.append(attempt)

    return hits
