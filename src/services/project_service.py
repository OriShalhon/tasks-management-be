from typing import Optional

from src.db.crud.project_crud import (
    addProject,
    deleteProject,
    getProject,
    updateProject,
)
from src.db.crud.task_crud import deleteTasks
from src.db.models.project_model import Project
from src.db.postgres import PostgresDB
from src.schemas.project_schema import ProjectData
from src.utils.utils import convert_tuple_to_model


def getProjectService(id: int, DB: PostgresDB) -> Optional[Project]:
    project_data = getProject(id, DB)
    if project_data:
        return convert_tuple_to_model(Project, project_data[0]).model_dump()
    return None

def addProjectService(Data: ProjectData, DB: PostgresDB) -> Project:
    project_id = addProject(Data, DB)
    return getProjectService(project_id, DB)

def updateProjectService(project_id: int, project_data: Project, DB: PostgresDB) -> Optional[Project]:
    updated_project = updateProject(DB, project_id, project_data)
    if updated_project:
        return Project(**updated_project)
    return None

def deleteProjectService(id: int, DB: PostgresDB) -> Optional[Project]:
    project_data = getProject(id, DB)
    if project_data:
        deleteTasks(id, DB)
        deleteProject(id, DB)
