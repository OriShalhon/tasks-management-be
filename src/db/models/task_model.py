from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TaskModel(BaseModel): 
    id: int 
    name: str 
    status: str 
    description: str 
    start_time: datetime
    attachment: str 
    blocking_task_id: Optional[int] = None
