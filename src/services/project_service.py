from typing import Optional

from src.db.crud.project_crud import (
    addProject,
    deleteProject,
    getProject,
    updateProject,
)
from src.db.crud.task_crud import deleteTasks
from src.db.postgres import PostgresDB
from src.schemas.project_schema import ProjectData, ProjectId


def addProjectService(project: ProjectData, DB: PostgresDB) -> ProjectData:
    addProject(DB, project)
    project_id = DB.get_last_inserted_id()
    return ProjectData(project_id=project_id, **project.dict())


def getProjectService(project_id: ProjectId, DB: PostgresDB) -> Optional[ProjectData]:
    project_data = getProject(DB, project_id)
    if project_data:
        return ProjectData(**project_data)
    return None


def updateProjectService(
    project_id: int, project_data: ProjectData, DB: PostgresDB
) -> Optional[ProjectData]:
    updated_project = updateProject(DB, project_id, project_data)
    if updated_project:
        return ProjectData(**updated_project)
    return None


def deleteProjectService(project_id: ProjectId, DB: PostgresDB) -> Optional[ProjectData]:
    project_data = getProject(project_id, DB)
    if project_data:
        deleteTasks(project_id, DB)
        deleteProject(project_id, DB)
        return ProjectData(**project_data)
    return None
