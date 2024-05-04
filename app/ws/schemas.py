from typing import List, Any
from pydantic import BaseModel


class Session(BaseModel):
    id: str
    users: List[str]


class Connection(BaseModel):
    id: str
    websocket: Any
