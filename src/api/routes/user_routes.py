from typing import Dict

from fastapi import APIRouter, Depends, HTTPException

from src.api.dependencies import get_DB
from src.schemas.users_schema import UserData, UserUpdate
from src.services.board_service import getUserBoardsService
from src.services.user_service import (
    deleteUserService,
    getUserIdService,
    signUpUserService,
    updateUserService,
)


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
def sign_up_endpoint(user: UserData, DB=Depends(get_DB)) -> None:
    signUpUserService(user, DB)


@router.put("/{id}")
def update_user_endpoint(
    id: int, user_update: UserUpdate, DB=Depends(get_DB)
) -> Dict[str, str]:
    return updateUserService(user_update, DB)


@router.delete("/{id}")
def delete_user_endpoint(user: UserData, DB=Depends(get_DB)) -> Dict[str, str]:
    return deleteUserService(user, DB)


@router.get("/{id}")
def get_user_endpoint(id: int, DB=Depends(get_DB)) -> Dict[str, str]:
    getUserIdService(id, DB)


# why is this in user routes rather than board routes?
@router.get("/{id}")
def get_user_boards_endpoint(id: int, DB=Depends(get_DB)) -> Dict:
    boards = getUserBoardsService(id, DB)
    if not boards:
        raise HTTPException(status_code=404, detail="No boards found for this user")
    return {"data": boards}
