from typing import Dict

from ...db.postgres import PostgresDB
from ...schemas.board_schema import boardId
from ...schemas.project_schema import ProjectData

TABLE_NAME = 'projects'

def getProjects(data: boardId, DB: PostgresDB) -> Dict:
    projects = DB.get_data(TABLE_NAME, ['project_id'], condition=('board_id', data.id))
    return projects