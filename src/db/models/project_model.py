from pydantic import BaseModel


class Project(BaseModel):
        id: int
        name: str
        visibility: bool
        board_id: int