from typing import Optional

from src.db.crud.task_crud import addTask, deleteTask, getTask, updateTask
from src.db.models.task_model import TaskModel
from src.db.postgres import PostgresDB
from src.schemas.tasks_schema import TaskData
from src.utils.utils import convert_tuple_to_model


def getTaskService(id: int, DB: PostgresDB) -> Optional[TaskModel]:
    taskData = getTask(id, DB)
    if taskData:
        return convert_tuple_to_model(TaskModel, taskData[0]).model_dump()
    return None


def addTaskService(task: TaskData, DB: PostgresDB) -> TaskModel:
    taskData = addTask(task, DB)
    if taskData:
        return convert_tuple_to_model(TaskModel, taskData[0]).model_dump()
    return None

def updateTaskService(id: int, task_data: TaskData, DB: PostgresDB) -> Optional[TaskData]:
    updated_task = updateTask(id, task_data, DB)
    if updated_task:
         return convert_tuple_to_model(TaskModel, updated_task[0]).model_dump()
    return None

def deleteTaskService(id: int, DB: PostgresDB) -> None:
    deleteTask(id, DB)
