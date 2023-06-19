"""application entry-point"""
import lib.io
from lib import placement
from lib import hit
from lib import draw
from lib.io import display_ship_inventory
from lib.models import Ship, Cell


def main() -> None:
    """entry-point function"""
    ships: dict[int, Ship] = placement.create_ships(lib.io.read_text())
    display_ship_inventory(ships)

    board: dict[Cell, int] = placement.fill_board(ships)
    attempts: list[Cell] = [
        Cell("F1"), Cell("A1"), Cell("A2"), Cell("A2"),
        Cell("B2"), Cell("C2"), Cell("B3"), Cell("D2"), Cell("E2"), Cell("F2"),
        Cell("H1"), Cell("H2"), Cell("H3"),
    ]
    successes: list[Cell] = hit.attempt_hits(attempts, board, ships)

    print("Game over -- here is the final map (+ == hit)")
    draw.generate_map(board, ships, successes)


if __name__ == "__main__":
    main()