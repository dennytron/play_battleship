"""application entry-point"""
from lib import placement
from lib import hit
from lib import draw
from lib import io
from lib.io import display_ship_inventory
from lib.models import Ship, Cell


def main() -> None:
    """entry-point function"""
    input_tokens: list[list[str]] = io.read_text()
    ships: dict[int, Ship] = placement.create_ships(input_tokens)
    display_ship_inventory(ships)

    board: dict[Cell, int] = placement.fill_board(ships)
    attempts: list[Cell] = io.get_shots(input_tokens)
    successes: list[Cell] = hit.attempt_hits(attempts, board, ships)

    print("Game over -- here is the final map (+ == hit)")
    draw.generate_map(board, ships, successes)


if __name__ == "__main__":
    main()
