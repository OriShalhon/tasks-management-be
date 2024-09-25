from typing import List, Optional

from src.db.models.task_model import task
from src.schemas.tasks_schema import TaskData, TaskId

from ..postgres import PostgresDB

TABLE_NAME = "tasks"


def addTask(data: TaskData, DB: PostgresDB) -> None:
    data_list = [
        {
            "name": data.name,
            "status": data.status,
            "description": data.description,
            "start_time": data.start_time,
            "attachment": data.attachment,
            "blocking_task_id": data.blocking_task_id,
            "project_id": data.project_id,
        }
    ]
    DB.write_data(TABLE_NAME, data_list)


def getTask(data: TaskId, DB: PostgresDB) -> task:
    # Retrieve board data from the database
    task_data = DB.get_data(
        TABLE_NAME,
        columns=[
            "task_id",
            "name",
            "status",
            "description",
            "start_time",
            "attachment",
            "blocking_task_id",
            "project_id",
        ],
        condition=("task_id", str(data.id)),
    )
    return task(*task_data[0])


def updateTask(id: TaskId, data: TaskData, DB: PostgresDB) -> Optional[TaskData]:
    update_data = {
        "name": data.name,
        "status": data.status,
        "description": data.description,
        "start_time": data.start_time,
        "attachment": data.attachment,
        "blocking_task_id": data.blocking_task_id,
        "project_id": data.project_id,
    }
    DB.update_data(TABLE_NAME, update_data, condition=("task_id", str(id.id)))
    updateData = getTask(id, DB)
    return updateData


def deleteTask(id: TaskId, DB: PostgresDB) -> None:
    DB.delete_data(TABLE_NAME, condition=("task_id", str(id.id)))


def getProjectTasks(project_id: int, DB: PostgresDB) -> List[task]:
    tasks_data = DB.get_data(
        TABLE_NAME,
        columns=[
            "task_id",
            "name",
            "status",
            "description",
            "start_time",
            "attachment",
            "blocking_task_id",
            "project_id",
        ],
        condition=("project_id", str(project_id.id)),
    )
    return [task(*task_data) for task_data in tasks_data]


def deleteTasks(project_id: int, DB: PostgresDB) -> None:
    DB.delete_data(TABLE_NAME, condition=("project_id", project_id))
