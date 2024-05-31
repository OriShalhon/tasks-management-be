import logging
import os
import uvicorn
from app.db.postgres import PostgresDB
from app import create_app

app = create_app()

logging.basicConfig(level=logging.INFO)

def setup_database(initiate_db: bool = False, populate_data: bool = False) -> None:
    db = PostgresDB()
    data_file = os.path.join(os.getcwd(), "projectTaskInfo.json")
    if initiate_db:
        db.initialize_db_structure()
    if populate_data:
        db.populate_db_from_file(data_file)


if __name__ == "__main__":
    setup_database(initiate_db=True, populate_data=True)
    logging.info("Starting the application")
    logging.info(f"app.state: {app.state.__dict__}")
    uvicorn.run(app, host="0.0.0.0", port=8000)
