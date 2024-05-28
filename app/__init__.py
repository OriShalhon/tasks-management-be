import logging

from fastapi import FastAPI
from app.db.postgres import PostgresDB
from contextlib import asynccontextmanager
from app.config import load_configuration, setup_logging

@asynccontextmanager
async def liftspan(app: FastAPI):
    try:
        logging.info("app startup")
        app.state.posgtres_manager = PostgresDB()

        yield
    except Exception as e:
        logging.error(e)
        raise e

def create_app() -> FastAPI:
    app = FastAPI()
    load_configuration(app)
    setup_logging()

    app.db = PostgresDB()

    return app