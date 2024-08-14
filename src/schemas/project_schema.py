from pydantic import BaseModel


class ProjectId(BaseModel):
    id: int


class ProjectData(BaseModel):
    name: str
    visibility: bool
    board_id: int