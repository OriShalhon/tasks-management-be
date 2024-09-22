from typing import Dict, List

from ...db.models.boards_model import Board
from ...schemas.board_schema import boardData, boardId
from ..postgres import PostgresDB

TABLE_NAME = 'boards'

def addBoard(board: boardData, DB: PostgresDB) -> None:
    data_list = [{'name':board.name, 'icon':board.icon, 'visibility': board.visibility, 'user_id': board.user_id}]
    DB.write_data(TABLE_NAME, data_list)

def getBoard(board: boardId, DB: PostgresDB) -> Dict:
    # Retrieve board data from the database
    board_data = DB.get_data(TABLE_NAME, columns=['board_id', 'name', 'icon', 'visibility', 'user_id'], condition=('board_id', board.id))
    board_dict = Board(*board_data[0])

    return board_dict
    
def getUserBoards(user_id: int, DB: PostgresDB) -> List[Dict]:
    boards_data = DB.get_data(TABLE_NAME, columns=['board_id', 'name', 'icon', 'visibility', 'user_id'], condition=('user_id', user_id))
    return [Board(*board_data) for board_data in boards_data]

