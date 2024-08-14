from typing import Dict

from fastapi import HTTPException

from ...schemas.users_schema import UserData, UserUpdate
from ..postgres import PostgresDB

TABLE_NAME = 'users'


def signUpUser(user: UserData, DB: PostgresDB) -> None:
    data_list = [{'email':user.email, 'username':user.username, 'password': user.password}]

    # Check if the email already exists
    existing_email = DB.get_data(TABLE_NAME, ['email'], condition=('email', user.email))
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already in use")
    
    data = DB.write_data(TABLE_NAME, data_list)

def getUserId(user: UserData, DB: PostgresDB) -> None:
    id = DB.get_data(TABLE_NAME, ['u_id'], condition=('email', user.email), fetchall=False)
    return id

def updateUser(user_update: UserUpdate, DB: PostgresDB) -> Dict[str, str]:    
    existing_user = DB.get_data(TABLE_NAME, ['username', 'password', 'email'], 
                                condition=('username', user_update.username))
    
    if not existing_user or existing_user[0][1] != user_update.current_password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    update_data = {}
    if user_update.new_email:
        # Check if the new email already exists
        existing_email = DB.get_data(TABLE_NAME, ['email'], condition=('email', user_update.new_email))
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already in use")
        update_data["email"] = user_update.new_email
    if user_update.new_username:
        update_data["username"] = user_update.new_username
    if user_update.new_password:
        update_data["password"] = user_update.new_password
    if not update_data:
        return {"message": "No updates requested"}
    
    # Update the user
    try:
        DB.update_data(TABLE_NAME, update_data, condition=('username', user_update.username))
        return {"message": "User updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    
    
def deleteUser(user: UserData, DB: PostgresDB) -> Dict[str, str]:    
    existing_user = DB.get_data(TABLE_NAME, ['username', 'password', 'email'], 
                                condition=('email', user.email))
    
    # Check if the user exists
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    try:
        DB.delete_data(TABLE_NAME, condition=('email', user.email))
        return {"message": "User delete successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")