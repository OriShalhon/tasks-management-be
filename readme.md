# Project Structure

This document outlines the architecture of our FastAPI-based application. Our project is structured to promote clarity, scalability, and separation of concerns.

## Directory Structure
```
├── src/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── board_router.py
│   │   │   ├── project_router.py
│   │   │   └── task_router.py
│   │   └── dependencies.py
│   │   
│   │
│   ├── core/
│   │   └── config.py
│   │   
│   │
│   ├── db/
│   │   ├── models/
│   │   │   ├── board.py
│   │   │   ├── project.py
│   │   │   └── task.py
│   │   ├── base.py
│   │   └── database.py
│   │
│   ├── schemas/
│   │   ├── board_schema.py
│   │   ├── project_schema.py
│   │   └── task_schema.py
│   │
│   ├── services/
│   │   ├── board_service.py
│   │   ├── project_service.py
│   │   └── task_service.py
│   │
│   └── main.py
│
├── tests/
│   ├── api/
│   ├── db/
│   └── services/
|
└── pyproject.toml
```

## Module Descriptions

- **api/routes**: Contains all route definitions, handling API requests and delegating business logic to the appropriate services.
- **core**: Manages core configurations and security settings for the application.
- **db/models**: Defines SQLAlchemy ORM models representing database tables.
- **db/database.py**: Manages database sessions and connections using dependency injection.
- **schemas**: Contains Pydantic schemas for request validation and response serialization.
- **services**: Implements the business logic of the application, used by route handlers.
- **main.py**: The entry point for the FastAPI application, setting up the application and including middleware.

## Testing

Tests are organized corresponding to the project structure to ensure each component functions correctly individually and integratively.
