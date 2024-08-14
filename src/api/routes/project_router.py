from typing import Dict

from fastapi import APIRouter, Depends

from src.api.dependencies import get_DB
from src.db.crud.project_crud import addProject, getProject

from ...schemas.project_schema import ProjectData, ProjectId

router = APIRouter(
    prefix="/project",
    tags=["project"],
    responses={404: {"description": "Not found"}},
)

@router.put("/addProject")
def add_project(project: ProjectData, DB = Depends(get_DB)) -> None:
    data = addProject(project, DB)
    return {"data": data}

@router.get("/getProject")
def get_project(project: ProjectId, DB = Depends(get_DB)) -> None:
    data = getProject(project, DB)
    return {"data": data}


