from typing import Optional

from src.db.crud.project_crud import (
    addProject,
    deleteProject,
    getProject,
    updateProject,
)
from src.db.crud.task_crud import deleteTasks
from src.db.postgres import PostgresDB
from src.schemas.project_schema import Project, ProjectId


def addProjectService(project: Project, DB: PostgresDB) -> Project:
    addProject(DB, project)
    project_id = DB.get_last_inserted_id()
    return Project(project_id=project_id, **project.dict())


def getProjectService(project_id: ProjectId, DB: PostgresDB) -> Optional[Project]:
    project_data = getProject(DB, project_id)
    if project_data:
        return Project(**project_data)
    return None


def updateProjectService(
    project_id: int, project_data: Project, DB: PostgresDB
) -> Optional[Project]:
    updated_project = updateProject(DB, project_id, project_data)
    if updated_project:
        return Project(**updated_project)
    return None


def deleteProjectService(project_id: ProjectId, DB: PostgresDB) -> Optional[Project]:
    project_data = getProject(project_id, DB)
    if project_data:
        deleteTasks(project_id, DB)
        deleteProject(project_id, DB)
        return Project(**project_data)
    return None
