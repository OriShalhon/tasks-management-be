from typing import Dict

from fastapi import APIRouter, Depends, HTTPException

from src.api.dependencies import get_DB
from src.db.crud.project_crud import addProject, getProject
from src.services.project_service import (
    addProjectService,
    deleteProjectService,
    getProjectService,
)

from ...schemas.project_schema import ProjectData, ProjectId

router = APIRouter(
    prefix="/project",
    tags=["project"],
    responses={404: {"description": "Not found"}},
)

@router.put("/addProject")
def add_project_endpoint(project: ProjectData, DB = Depends(get_DB)) -> None:
    data = addProjectService(project, DB)
    return {"data": data}

@router.get("/getProject")
def get_project_endpoint(project: ProjectId, DB = Depends(get_DB)) -> Dict:
    project = getProjectService(project.id, DB)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"data": project}

@router.get("/deleteProject")
def delete_project_endpoint(project: ProjectId, DB = Depends(get_DB)) -> Dict:
    project = deleteProjectService(project.id, DB)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"data": project}




