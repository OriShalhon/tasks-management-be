import os
import psycopg2

from app.utils.singleton import Singleton

class PostgresDB(Singleton):
    def __init__(self):
        connection_string = os.getenv("DATABASE_URL")
        self.conn = psycopg2.connect(connection_string)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name : str , columns : dict) -> None:
        # Create a new table with the given name and columns
        columns_str = ", ".join(f"{name} {type}" for name, type in columns.items())
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
        self.cursor.execute(query)
        self.conn.commit()

    def write_data(self, table_name : str, data_list : list[dict]) -> None:
        # Write new data to the specified table
        for data in data_list:
            columns_str = ", ".join(data.keys())
            values_str = ", ".join("%s" for _ in data.values())
            query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"
            self.cursor.execute(query, tuple(data.values()))
        self.conn.commit()


def initialize_db_structure(db):
    pass

if __name__ == "__main__":
    db = PostgresDB()
    initialize_db_structure(db)
