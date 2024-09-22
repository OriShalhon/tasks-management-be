from typing import Dict

from fastapi import APIRouter, Depends, HTTPException

from src.api.dependencies import get_DB
from src.schemas.board_schema import boardId
from src.schemas.users_schema import UserData, UserUpdate
from src.services.board_service import getUserBoardsService
from src.services.user_service import (
    deleteUserService,
    getUserIdService,
    signUpUserService,
)

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.put("/signUp")
def sign_up_endpoint(user: UserData, DB=Depends(get_DB)) -> None:
    signUpUserService(user, DB)


@router.put("/updateUser")
def update_user_endpoint(user_update: UserUpdate, DB=Depends(get_DB)) -> Dict[str, str]:
    return getUserIdService(user_update, DB)


@router.delete("/deleteUser")
def delete_user_endpoint(user: UserData, DB=Depends(get_DB)) -> Dict[str, str]:
    return deleteUserService(user, DB)


@router.get("/getUserBoards")
def get_user_boards_endpoint(user_id: boardId, DB=Depends(get_DB)) -> Dict:
    boards = getUserBoardsService(user_id, DB)
    if not boards:
        raise HTTPException(status_code=404, detail="No boards found for this user")
    return {"data": boards}
