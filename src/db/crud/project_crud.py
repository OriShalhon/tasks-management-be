from typing import Dict, Optional

from ...db.models.project_model import Project
from ...schemas.project_schema import ProjectData, ProjectId
from ..postgres import PostgresDB

TABLE_NAME = 'projects'

def addProject(project: ProjectData, DB: PostgresDB) -> None:
    data_list = [{'name':project.name, 'visibility': project.visibility, 'board_id': project.board_id}]
    DB.write_data(TABLE_NAME, data_list)

def getProject(project: ProjectId, DB: PostgresDB) -> Dict:
    # Retrieve board data from the database
    project_data = DB.get_data(TABLE_NAME, columns=['project_id', 'name', 'visibility', 'board_id'], condition=('project_id', project.id))
    project_dict = Project(*project_data[0])

    return project_dict

def updateProject(DB: PostgresDB, project_id: int, project_data: ProjectData) -> Optional[Dict]:
    update_data = {'name': project_data.name, 'visibility': project_data.visibility, 'board_id': project_data.board_id}
    DB.update_data(TABLE_NAME, update_data, condition=('project_id', project_id))
    return getProject(project_id, DB)

def deleteProject(project_id: int, DB: PostgresDB) -> None:
    DB.delete_data(TABLE_NAME, condition=('project_id', project_id))