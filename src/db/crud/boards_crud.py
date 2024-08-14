from typing import Dict

from ...db.models.boards_model import Boards
from ...schemas.board_schema import boardData, boardId
from ..postgres import PostgresDB

TABLE_NAME = 'boards'

def addBoard(board: boardData, DB: PostgresDB) -> None:
    data_list = [{'name':board.name, 'icon':board.icon, 'visibility': board.visibility, 'user_id': board.user_id}]
    
    data = DB.write_data(TABLE_NAME, data_list)

def getBoard(board: boardId, DB: PostgresDB) -> Dict:
    # Retrieve board data from the database
    board_data = DB.get_data(TABLE_NAME, columns=['board_id', 'name', 'icon', 'visibility', 'user_id'], condition=('board_id', board.id))
    board_dict = Boards(*board_data[0])

    return board_dict

