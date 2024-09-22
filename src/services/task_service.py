from typing import Optional

from src.db.crud.task_crud import addTask, deleteTask, getTask, updateTask
from src.db.models.task_model import task
from src.db.postgres import PostgresDB
from src.schemas.tasks_schema import TaskData, TaskId


def addTaskService(task: TaskData, DB: PostgresDB) -> task:
    addTask(DB, task)


def getTaskService(task_id: TaskId, DB: PostgresDB) -> Optional[task]:
    taskData = getTask(DB, task_id)
    if taskData:
        return task(**taskData)
    return None


def updateTaskService(
    task_id: TaskId, task_data: TaskData, DB: PostgresDB
) -> Optional[TaskData]:
    updated_task = updateTask(task_id, task_data, DB)
    if updated_task:
        return updated_task
    return None


def deleteTaskService(task_id: TaskId, DB: PostgresDB) -> None:
    deleteTask(task_id, DB)
