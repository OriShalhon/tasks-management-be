from typing import Dict

from fastapi import APIRouter, Depends

from src.api.dependencies import get_DB
from src.db.crud.user_crud import deleteUser, signUpUser, updateUser
from src.schemas.users_schema import UserData, UserUpdate

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

@router.put("/signUp")
def sign_Up(user: UserData, DB = Depends(get_DB)) -> None:
    signUpUser(user, DB)

@router.put("/updateUser")
def update_user(user_update: UserUpdate, DB = Depends(get_DB)) -> Dict[str, str]:
    return updateUser(user_update, DB)

@router.delete("/deleteUser")
def delete_user(user: UserData, DB = Depends(get_DB)) -> Dict[str, str]:
    return deleteUser(user, DB)