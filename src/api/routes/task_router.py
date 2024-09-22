from typing import Dict, List, Optional

from fastapi import APIRouter, Depends

from src.api.dependencies import (
    get_DB,  # Assuming this dependency fetches your database connection
)
from src.schemas.tasks_schema import TaskData, TaskId
from src.services.task_service import (
    addTaskService,
    deleteTaskService,
    getTaskService,
    updateTaskService,
)

router = APIRouter(
    prefix="/task",
    tags=["task"],
    responses={404: {"description": "Not found"}},
)


@router.post("/createTask")
async def create_task_endpoint(task: TaskData, DB=Depends(get_DB)) -> TaskData:
    addTaskService(task, DB)

@router.get("/getTask")
async def get_task_endpoint(id: TaskId, DB=Depends(get_DB)) -> Dict:
    taskModel = getTaskService(id, DB)
    return taskModel.to_dict()

@router.put("/updateTask")
async def update_task_endpoint(id: TaskId, updated_task: TaskData, DB=Depends(get_DB)) -> Optional[TaskData]:
    return updateTaskService(id, updated_task, DB)

@router.delete("/deleteTask")
async def delete_task_endpoint(id: TaskId, DB=Depends(get_DB)) -> None:
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