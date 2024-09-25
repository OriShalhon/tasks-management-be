from pydantic import BaseModel


class boardId(BaseModel):
    id: int


class boardData(BaseModel):
    name: str
    icon: str
    visibility: bool
    user_id: int
