from typing import Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException

from src.api.dependencies import (
    get_DB,  # Assuming this dependency fetches your database connection
)
from src.schemas.tasks_schema import TaskData
from src.services.task_service import (
    addTaskService,
    deleteTaskService,
    getTaskService,
    updateTaskService,
)

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{id}")
async def get_task_endpoint(id: int, DB=Depends(get_DB)) -> Dict:
    taskModel = getTaskService(id, DB)
    if not taskModel:
        raise HTTPException(status_code=404, detail="Task not found")
    return taskModel

@router.post("/")
async def create_task_endpoint(task: TaskData, DB=Depends(get_DB)) -> Dict:
    taskModel = addTaskService(task, DB)
    if not taskModel:
        raise HTTPException(status_code=404, detail="Task not found")
    return taskModel

@router.put("/{id}")
async def update_task_endpoint(id: int, updated_task: TaskData, DB=Depends(get_DB)) -> Optional[TaskData]:
    taskModel = updateTaskService(id, updated_task, DB)
    if not taskModel:
        raise HTTPException(status_code=404, detail="Task not found")
    return taskModel

@router.delete("/{id}")
async def delete_task_endpoint(id: int, DB=Depends(get_DB)) -> None:
    deleteTaskService(id, DB)

"""
@router.get("/getProjectTasks")
async def get_project_tasks(id: TaskId, DB=Depends(get_DB)) -> List:
    tasks = task_crud.getProjectTasks(id, DB)
    taskList = [task.to_dict() for task in tasks]
    taskIdList = []
    for task in taskList:
        taskIdList.append(task['id'])
    return taskIdList
"""