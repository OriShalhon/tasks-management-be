from typing import Dict, List, Optional

from src.db.models.task_model import TaskModel
from src.schemas.tasks_schema import TaskData

from ..postgres import PostgresDB

TABLE_NAME = 'tasks'

def addTask(data: TaskData, DB: PostgresDB) -> None:
    data_list = [{'name':data.name, 'status':data.status, 'description':data.description, 'start_time':data.start_time,
                   'attachment':data.attachment, 'blocking_task_id':data.blocking_task_id, 'project_id':data.project_id}]
    id = DB.write_data(TABLE_NAME, data_list)
    taskData = getTask(id, DB)
    return taskData


def getTask(data: int, DB: PostgresDB) -> TaskModel:
    # Retrieve board data from the database
    task_data = DB.get_data(TABLE_NAME, columns=['task_id', 'name', 'status', 'description','start_time',
                                                 'attachment', 'blocking_task_id', 'project_id'], condition=('task_id', str(data)))
    return task_data

def updateTask(id: int, data: TaskData, DB: PostgresDB) -> Optional[TaskData]:
    update_data = {'name': data.name, 'status': data.status, 'description': data.description, 'start_time': data.start_time,
                   'attachment': data.attachment, 'blocking_task_id': data.blocking_task_id, 'project_id': data.project_id}
    DB.update_data(TABLE_NAME, update_data, condition=('task_id', str(id.id)))
    updateData = getTask(id, DB)
    return updateData

def deleteTask(id: int, DB: PostgresDB) -> None:
    DB.delete_data(TABLE_NAME, condition=('task_id', str(id.id)))

def getProjectTasks(project_id: int, DB: PostgresDB) -> List[TaskModel]:
    tasks_data = DB.get_data(TABLE_NAME, columns=['task_id', 'name', 'status', 'description', 'start_time',
                                                  'attachment', 'blocking_task_id', 'project_id'], condition=('project_id', str(project_id.id)))
    return [TaskModel(*task_data) for task_data in tasks_data]

def deleteTasks(project_id: int, DB: PostgresDB) -> None:
    DB.delete_data(TABLE_NAME, condition=('project_id', project_id))