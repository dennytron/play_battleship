"""functions managing the placement of ships"""
from lib.models import INTS_TO_LETTERS, SHIP_TYPES, Ship, Cell


def fill_board(ships: dict[int, Ship]) -> dict[Cell, int]:
    """populate the board with ships"""
    board: dict[Cell, int] = {}
    for ship in ships.values():
        for cell in place_ship(ship, ships, board):
            board[cell] = ship.key
    return board


def place_ship(ship: Ship, ships: dict[int, Ship], board: dict[Cell, int]) -> list[Cell]:
    """this function returns a list of the cells on the board occupied by the ship"""
    start_cell: Cell = Cell(ship.start)
    start_x: int = start_cell.x_value
    start_y: int = start_cell.y_as_int
    current_ship_cells: list[Cell] = _generate_cells(ship, start_x, start_y)
    placement_is_valid: bool = _ship_placement_is_valid(ship, current_ship_cells, board, ships)

    if not placement_is_valid:
        return []

    return current_ship_cells


def _generate_cells(ship, start_x, start_y) -> list[Cell]:
    """generate the cells that the ship occupies"""
    if ship.direction == "right":
        return [_get_cell(start_y, start_x + n) for n in range(0, ship.size)]
    if ship.direction == "down":
        return [_get_cell(start_y + n, start_x) for n in range(0, ship.size)]

    print(f"Warning! Direction not implemented! {ship.direction}")
    return []


def _get_cell(y_value: int, x_value: int) ->  Cell:
    """retrieve the cell at the xy location"""
    str_cell: str = INTS_TO_LETTERS[y_value] + str(x_value)
    return Cell(str_cell)


def _ship_placement_is_valid(
        current_ship: Ship,
        current_ship_cells: list[Cell],
        board: dict[Cell, int],
        all_ships: dict[int, Ship]) -> bool:
    """verify whether the ship is allowed to be placed on the board"""
    for cell in current_ship_cells:
        cell_is_occupied: bool = cell in board
        ship_is_out_of_bounds: bool = cell.y_as_int > 10 or cell.x_value > 10

        if cell_is_occupied:
            # verify whether a ship is being placed at a location already occupied
            ship_key: int = board[cell]
            existing: Ship = all_ships[ship_key]
            print(
                f"Error placing ship {current_ship.start} / {current_ship.direction} - "
                f"Cell occupied at cell={cell.location} "
                f"by ship => {existing.start} / {existing.direction}"
            )
            return False

        if ship_is_out_of_bounds:
            # verify whether the player is placing a ship off the board
            print(
                f"Error placing ship "
                f"{current_ship.start} / {current_ship.direction} "
                f"- Ship off board! {cell.location}"
            )
            return False

    return True


def _get_size(ship_type: str) -> int:
    """fetch the number of hits a ship can take based on the ship type"""
    assert ship_type.lower() in SHIP_TYPES
    return SHIP_TYPES[ship_type]


def create_ships(lines: list[list[str]]) -> dict[int, Ship]:
    """parse the input text file; return a list of ship information"""
    ships: dict[int, Ship] = {
        key: Ship(
            key=key,
            size=_get_size(tokens[1].lower()),
            direction=tokens[2].lower(),
            kind=tokens[1],
            start=tokens[3].upper()
        )
        for key, tokens in enumerate(lines)
        if tokens[0].upper() == "PLACE_SHIP"
    }
    assert ships
    return ships
