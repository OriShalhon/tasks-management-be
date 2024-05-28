import logging

import uvicorn

from app import create_app

app = create_app()

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.info("Starting the application")
    logging.info(f"app.state: {app.state.__dict__}")
    uvicorn.run(app, host="0.0.0.0", port=8000)
