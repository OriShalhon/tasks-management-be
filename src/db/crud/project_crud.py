from typing import Dict

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