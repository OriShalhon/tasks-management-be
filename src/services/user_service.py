from typing import Dict

from fastapi import HTTPException

from src.db.crud.user_crud import deleteUser, getUserId, signUpUser, updateUser
from src.db.postgres import PostgresDB
from src.schemas.users_schema import UserData, UserUpdate


def signUpUserService(user: UserData, DB: PostgresDB) -> None:
    signUpUser(user, DB)

def getUserIdService(user: UserData, DB: PostgresDB) -> int:
    user_id = getUserId(user, DB)
    if not user_id:
        raise HTTPException(status_code=404, detail="User not found")
    return user_id

def updateUserService(user_update: UserUpdate, DB: PostgresDB) -> Dict[str, str]:
    return updateUser(user_update, DB)

def deleteUserService(user: UserData, DB: PostgresDB) -> Dict[str, str]:
    return deleteUser(user, DB)