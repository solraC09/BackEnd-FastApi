from pydantic import BaseModel
from typing import Optional


class TasksCreate(BaseModel):
    titulo: str
    descricao: Optional[str] = None


class TasksResponse(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str]
    concluida: bool

    class Config:
        from_attributes = True