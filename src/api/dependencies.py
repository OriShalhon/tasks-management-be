from fastapi import Request

from src.db.postgres import PostgresDB


def get_DB(request: Request) -> PostgresDB:
    return request.app.state.postgres_manager
