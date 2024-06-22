import logging
import os

from fastapi import FastAPI
from dotenv import load_dotenv


def load_configuration(app: FastAPI):
    load_dotenv()
    # this will be used to setup the configuration and state of the application


def setup_logging():
    log_file = os.path.join(os.getcwd(), "app.log")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
    )
