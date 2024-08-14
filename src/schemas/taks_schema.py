from pydantic import BaseModel


class taskId(BaseModel):
    id: int


class taskData(taskId):
    name: str
    status: str
    description: str
    start_time: str
    attachment: str
    blocking_task_id: int
    project_id: int
    
    