import os
import psycopg2

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
                "id": "SERIAL PRIMARY KEY",
                "email": "VARCHAR(255)",
                "username": "VARCHAR(255)",
                "password": "VARCHAR(255)",
            },
            "boards": {
                "board_id": "SERIAL PRIMARY KEY",
                "name": "VARCHAR(255)",
                "icon": "VARCHAR(255)",
                "visibility": "BOOLEAN",
                "user_id": "INTEGER REFERENCES users(id)",
            },
            "projects": {
                "project_id": "SERIAL PRIMARY KEY",
                "name": "VARCHAR(255)",
                "visibility": "BOOLEAN",
                "board_id": "INTEGER REFERENCES boards(board_id)",
            },
            "tasks": {
                "id": "SERIAL PRIMARY KEY",
                "name": "VARCHAR(255)",
                "status": "VARCHAR(255)",
                "description": "TEXT",
                "start_time": "TIMESTAMP",
                "attachment": "TEXT",
                "blocking_task_id": "INTEGER REFERENCES tasks(id)",
                "project_id": "INTEGER REFERENCES projects(project_id)",
            },
        }

        # Create the tables
        for table_name, columns in tables.items():
            self.create_table(table_name, columns)


if __name__ == "__main__":
    db = PostgresDB()
    db.initialize_db_structure()
