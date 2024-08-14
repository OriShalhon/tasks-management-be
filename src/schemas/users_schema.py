from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    password: str

class UserData(UserBase):
    email: EmailStr

class UserUpdate(UserBase):
    new_username: str | None = None
    new_password: str | None = None
    new_email: EmailStr | None = None