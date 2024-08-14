from typing import Dict

from fastapi import APIRouter, Depends

from src.api.dependencies import get_DB
from src.db.crud.boards_crud import addBoard, getBoard
from src.db.models.project import getProjects

from ...db.postgres import PostgresDB
from ...schemas.board_schema import boardData, boardId

router = APIRouter(
    prefix="/board",
    tags=["board"],
    responses={404: {"description": "Not found"}},
)

@router.put("/addBoard")
def add_board(board: boardData, DB = Depends(get_DB)) -> None:
    data = addBoard(board, DB)
    return {"data": data}


@router.get("/getBoard")
def get_board(board: boardId, DB = Depends(get_DB)) -> None:
    data = getBoard(board, DB)
    return {"data": data}

"""
@router.get("/userBords")
def get_bords(user: UserData, DB = Depends(get_DB)) -> Dict:
    data = getUserBords(user, DB)
    return {"data": data}
"""

def getBordsProjects(data: boardId, DB: PostgresDB) -> Dict:
    projects = getProjects(data, DB)
    return projects