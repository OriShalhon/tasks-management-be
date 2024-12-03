from typing import List, Optional

from src.db.crud.boards_crud import addBoard, getBoard, getUserBoards
from src.db.models.boards_model import Board
from src.db.postgres import PostgresDB
from src.schemas.board_schema import boardData
from src.utils.utils import convert_tuple_to_model


def addBoardService(board: boardData, DB: PostgresDB) -> Board:
    addBoard(board, DB)


def getBoardService(board_id: int, DB: PostgresDB) -> Optional[Board]:
    board_data = getBoard(board_id, DB)
    if board_data:
        return convert_tuple_to_model(Board, board_data[0]).model_dump()
    return None


def getUserBoardsService(user_id: int, DB: PostgresDB) -> List[Board]:
    boards_data = getUserBoards(user_id, DB)
    return [Board(**board.dict()) for board in boards_data]
