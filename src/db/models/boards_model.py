from pydantic import BaseModel


class Board(BaseModel):
    id: int
    name: str
    icon: str
    visibility: bool
    user_id: int
