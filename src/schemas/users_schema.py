from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    password: str


class UserData(UserBase):
    email: EmailStr


class UserUpdate(UserBase):
    new_username: Optional[str] = None
    new_password: Optional[str] = None
    new_email: Optional[EmailStr] = None
