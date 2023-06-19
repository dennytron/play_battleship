"""functions managing the placement of ships"""
from lib.models import VERTICAL_INTS_TO_LETTERS, SHIP_TYPES, Ship, Cell


def fill_board(ships: dict[int, Ship]) -> dict[Cell, int]:
    """populate the board with ships"""
    board: dict[Cell, int] = {}
    for ship in ships.values():
        for cell in place_ship(ship, ships, board):
            board[cell] = ship.key
    return board


def place_ship(ship: Ship, ships: dict[int, Ship], board: dict[Cell, int]) -> list[Cell]:
    """this function returns a dictionary of yx location keys and int primary key"""
    start_cell: Cell = Cell(ship.start)
    start_x: int = start_cell.x_value
    start_y: int = start_cell.y_as_int
    current_ship_cells: list[Cell] = _generate_cells(ship, start_x, start_y)
    _verify_ship_placement(current_ship_cells, board, ship, ships)
    return current_ship_cells


def _generate_cells(ship, start_x, start_y) -> list[Cell]:
    """generate the cells that the ship occupies"""
    if ship.direction == "right":
        return [_get_cell(start_y, start_x + n) for n in range(0, ship.size)]
    if ship.direction == "down":
        return [_get_cell(start_y + n, start_x) for n in range(0, ship.size)]
    raise NotImplementedError(f"Direction not implemented! {ship.direction}")


def _get_cell(y_value: int, x_value: int) ->  Cell:
    """retrieve the cell at the xy location"""
    str_cell: str = VERTICAL_INTS_TO_LETTERS[y_value] + str(x_value)
    return Cell(str_cell)


def _verify_ship_placement(
        current_ship_cells: list[Cell],
        board: dict[Cell, int],
        current_ship: Ship,
        all_ships: dict[int, Ship]):
    """verify whether the ship is allowed to be placed on the board"""
    cell: Cell

    for cell in current_ship_cells:
        cell_is_occupied: bool = cell in board
        ship_is_out_of_bounds: bool = cell.y_as_int > 10 or cell.x_value > 10

        if cell_is_occupied:
            # verify whether a ship is being placed at a location already occupied
            # raise an exception if the cell is already occupied
            ship_key: int = board[cell]
            existing: Ship = all_ships[ship_key]
            raise NotImplementedError(
                f"Error placing ship {current_ship.start} / {current_ship.direction} - "
                f"Cell occupied at cell={cell.location} "
                f"by ship => {existing.start} / {existing.direction}"
            )

        if ship_is_out_of_bounds:
            # verify whether the player is placing a ship off the board
            # should these ships be redirected to another file?
            raise NotImplementedError(
                f"Error placing ship "
                f"{current_ship.start} / {current_ship.direction} "
                f"- Ship off board! {cell}"
            )


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
