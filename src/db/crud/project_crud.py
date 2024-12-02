"""
This module contains CRUD (Create, Read, Update, Delete) operations for managing projects in the database.

It provides functions to add, retrieve, update, and delete project data using a PostgreSQL database.
The module interacts with the 'projects' table in the database.

Functions:
    addProject: Add a new project to the database.
    getProject: Retrieve project data from the database.
    updateProject: Update an existing project in the database.
    deleteProject: Delete a project from the database.

Each function takes a PostgresDB object as a parameter to perform database operations.
"""
from typing import Dict, Optional

from ...schemas.project_schema import ProjectData
from ..postgres import PostgresDB

TABLE_NAME = 'projects'

def getProject(id: int, DB: PostgresDB) -> Dict:
    # Retrieve board data from the database
    project_data = DB.get_data(TABLE_NAME, columns=['project_id', 'name', 'visibility', 'board_id'], condition=('project_id', id))
    return project_data

def addProject(data: ProjectData, DB: PostgresDB) -> None:
    data_list = [{'name':data.name, 'visibility': data.visibility, 'board_id': data.board_id}]
    return DB.write_data(TABLE_NAME, data_list)

def updateProject(DB: PostgresDB, project_id: int, project_data: ProjectData) -> Optional[Dict]:
    update_data = {'name': project_data.name, 'visibility': project_data.visibility, 'board_id': project_data.board_id}
    DB.update_data(TABLE_NAME, update_data, condition=('project_id', project_id))
    return getProject(project_id, DB)


def deleteProject(project_id: int, DB: PostgresDB) -> None:
    DB.delete_data(TABLE_NAME, condition=('project_id', project_id))


