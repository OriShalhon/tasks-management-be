from typing import Dict

from fastapi import APIRouter, Depends, HTTPException

from src.api.dependencies import get_DB
from src.services.project_service import (
    addProjectService,
    deleteProjectService,
    getProjectService,
    updateProjectService,
)

from ...schemas.project_schema import ProjectData

router = APIRouter(
    prefix="/projects",
    tags=["projects"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
def add_project_endpoint(project: ProjectData, DB=Depends(get_DB)) -> None:
    data = addProjectService(project, DB)
    return data


@router.get("/{id}")
def get_project_endpoint(id: int, DB=Depends(get_DB)) -> Dict:
    project = getProjectService(id, DB)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.put("/{id}")
def update_project_endpoint(id: int, project: ProjectData, DB=Depends(get_DB)) -> None:
    updated_project = updateProjectService(id, project, DB)
    if not updated_project:
        raise HTTPException(status_code=404, detail="Project not found")


@router.delete("/")
def delete_project_endpoint(id: int, DB=Depends(get_DB)) -> None:
    deleteProjectService(id, DB)
