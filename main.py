import logging
import os
from typing import Dict

import uvicorn
from fastapi import Depends

from src import create_app
from src.api.dependencies import get_DB
from src.api.routes import board_router, project_router, task_router, user_routes
from src.api.routes.board_router import getBordsProjects
from src.db.postgres import PostgresDB
from src.schemas.get_data_schema import Data

app = create_app()

# ---- Do this for all of your routes ----
app.include_router(user_routes.router)
app.include_router(board_router.router)
app.include_router(project_router.router)
app.include_router(task_router.router)
# ----------------------------------------

logging.basicConfig(level=logging.INFO)


def setup_database(initiate_db: bool = False, populate_data: bool = False) -> None:
    db = PostgresDB()
    data_file = os.path.join(os.getcwd(), "projectTaskInfo.json")
    if initiate_db:
        db.initialize_db_structure()
    if populate_data:
        db.populate_db_from_file(data_file)

@app.get("/GetData")
def get_data(data: Data, DB = Depends(get_DB)) -> dict:  
    data = DB.get_data(data.table, data.column, 
                       [data.condition_column, data.condition] 
                       if data.condition else None)
    print(data)
    return {"data": data}

@app.get("/getProjects")
def getProjects(data: int, DB = Depends(get_DB)) -> Dict:
    data = getBordsProjects(data, DB)
    return {"data": data}


if __name__ == "__main__":
    logging.info("Starting the application")
    logging.info(f"app.state: {app.state.__dict__}")
    uvicorn.run(app, host="127.0.0.1", port=8000)
