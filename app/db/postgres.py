import os
import psycopg2
import json
from app.utils.singleton import Singleton


class PostgresDB(Singleton):
    def __init__(self):
        connection_string = os.getenv("DATABASE_URL")
        self.conn = psycopg2.connect(connection_string)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name: str, columns: dict) -> None:
        # Create a new table with the given name and columns
        columns_str = ", ".join(f"{name} {type}" for name, type in columns.items())
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
        self.cursor.execute(query)
        self.conn.commit()

    def write_data(self, table_name: str, data_list: list[dict]) -> None:
        # Write new data to the specified table
        for data in data_list:
            columns_str = ", ".join(data.keys())
            values_str = ", ".join("%s" for _ in data.values())
            query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"
            self.cursor.execute(query, tuple(data.values()))
        self.conn.commit()

    def initialize_db_structure(self):
        # Define the structure of the tables
        tables = {
            "users": {
                "u_id": "SERIAL PRIMARY KEY",
                "email": "VARCHAR(255)",
                "username": "VARCHAR(255)",
                "password": "VARCHAR(255)",
            },
            "boards": {
                "board_id": "SERIAL PRIMARY KEY",
                "name": "VARCHAR(255)",
                "icon": "VARCHAR(255)",
                "visibility": "BOOLEAN",
                "user_id": "INTEGER REFERENCES users(u_id)",
            },
            "projects": {
                "project_id": "SERIAL PRIMARY KEY",
                "name": "VARCHAR(255)",
                "visibility": "BOOLEAN",
                "board_id": "INTEGER REFERENCES boards(board_id)",
            },
            "tasks": {
                "task_id": "SERIAL PRIMARY KEY",
                "name": "VARCHAR(255)",
                "status": "VARCHAR(255)",
                "description": "TEXT",
                "start_time": "TIMESTAMP",
                "attachment": "TEXT",
                "blocking_task_id": "INTEGER REFERENCES tasks(task_id)",
                "project_id": "INTEGER REFERENCES projects(project_id)",
            },
        }

        # Create the tables
        for table_name, columns in tables.items():
            self.create_table(table_name, columns)

    def populate_db_from_file(self, data_file: str) -> None:
        # Load data from JSON file
        with open(data_file, "r") as f:
            data = json.load(f)

        # Iterate over boards
        for board in data["boards"]:
            # Insert board
            self.write_data(
                "boards",
                [
                    {
                        "board_id": board["id"],
                        "name": board["boardName"],
                        "icon": board["icon"],
                        "visibility": board["isVisible"],
                    }
                ],
            )

            # Iterate over projects
            for project in board["projects"]:
                # Insert project
                self.write_data(
                    "projects",
                    [
                        {
                            "project_id": project["id"],
                            "name": project["projectName"],
                            "visibility": project["isVisible"],
                            "board_id": board["id"],
                        }
                    ],
                )

                # Iterate over tasks
                for task in project["tasks"]:
                    # Insert task
                    self.write_data(
                        "tasks",
                        [
                            {
                                "task_id": task["id"],
                                "name": task["headline"],
                                "status": task["status"],
                                "description": task["description"],
                                "project_id": project["id"],
                                "blocking_task_id": task["blocking_task_id"]
                                if "blocking_task_id" in task
                                else None,
                            }
                        ],
                    )
