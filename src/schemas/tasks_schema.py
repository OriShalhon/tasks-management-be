from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TaskData(BaseModel):
    name: str
    status: int
    description: Optional[str] = None
    start_time: Optional[datetime] = None
    attachment: Optional[str] = None
    blocking_task_id: Optional[int] = None
    project_id: int
    
    