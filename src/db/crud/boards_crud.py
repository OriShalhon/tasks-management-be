from typing import Dict, List

from ...schemas.board_schema import boardData
from ..postgres import PostgresDB

TABLE_NAME = "boards"


def addBoard(board: boardData, DB: PostgresDB) -> None:
    data_list = [
        {
            "name": board.name,
            "icon": board.icon,
            "visibility": board.visibility,
            "user_id": board.user_id,
        }
    ]
    DB.write_data(TABLE_NAME, data_list)


def getBoard(board: int, DB: PostgresDB) -> Dict:
    # Retrieve board data from the database
    board_data = DB.get_data(
        TABLE_NAME,
        columns=["board_id", "name", "icon", "visibility", "user_id"],
        condition=("board_id", board),
    )
    return board_data


def getUserBoards(user_id: int, DB: PostgresDB) -> List[Dict]:
    boards_data = DB.get_data(
        TABLE_NAME,
        columns=["board_id", "name", "icon", "visibility", "user_id"],
        condition=("user_id", user_id),
    )
    # return [Board(*board_data) for board_data in boards_data]
