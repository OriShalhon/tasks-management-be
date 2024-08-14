from pydantic import BaseModel


class Data(BaseModel):
    table: str
    column: str = '*'
    condition_column: str = None
    condition: str = None