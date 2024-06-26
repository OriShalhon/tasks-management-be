import logging
import os

import uvicorn
from fastapi import Response

from src import create_app
from src.db.postgres import PostgresDB

app = create_app()

logging.basicConfig(level=logging.INFO)


def setup_database(initiate_db: bool = False, populate_data: bool = False) -> None:
    db = PostgresDB()
    data_file = os.path.join(os.getcwd(), "projectTaskInfo.json")
    if initiate_db:
        db.initialize_db_structure()
    if populate_data:
        db.populate_db_from_file(data_file)

@app.get("/{table}/{column}/{condition}")
def get_data(table: str, column: str,  condition: str, response : Response):
    db = PostgresDB()
    data = db.get_data(table, '*', [column, condition])
    return {"data": data}



if __name__ == "__main__":
    logging.info("Starting the application")
    logging.info(f"app.state: {app.state.__dict__}")
    uvicorn.run(app, host="127.0.0.1", port=8001)
