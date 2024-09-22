from typing import Optional

from pydantic import BaseModel


class TaskId(BaseModel):
    id: int


class TaskData(BaseModel):
    name: str
    status: int
    description: str
    start_time: Optional[str]
    attachment: str
    blocking_task_id: Optional[int]
    project_id: int
    
    