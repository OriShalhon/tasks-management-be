from pydantic import BaseModel


class boardData(BaseModel):
    name: str
    icon: str
    visibility: bool
    user_id: int
    