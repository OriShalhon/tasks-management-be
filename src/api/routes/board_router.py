from typing import Dict

from fastapi import APIRouter, Depends, HTTPException

from src.api.dependencies import get_DB
from src.schemas.board_schema import boardData, boardId
from src.services.board_service import addBoardService, getBoardService

router = APIRouter(
    prefix="/board",
    tags=["board"],
    responses={404: {"description": "Not found"}},
)

@router.put("/addBoard")
def add_board_endpoint(board: boardData, DB = Depends(get_DB)) -> Dict:
    data = addBoardService(board, DB)
    return {"data": data}


@router.get("/getBoard")
def get_board_endpoint(board: boardId, DB = Depends(get_DB)) -> Dict:
    board = getBoardService(board.id, DB)
    if board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return {"data": board}

"""
def getBordsProjects(data: boardId, DB: PostgresDB) -> Dict:
    projects = getProjects(data, DB)
    return projects

"""