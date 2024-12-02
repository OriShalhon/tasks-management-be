from pydantic import BaseModel


class ProjectData(BaseModel):
    name: str
    visibility: bool
    board_id: int
