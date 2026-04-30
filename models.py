from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import create_engine, String, Integer, Boolean
from database import Base

db = create_engine("sqlite:///banco.db")

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )
    titulo: Mapped[str] = mapped_column(
        String(100), nullable=False
    )
    descricao: Mapped[str] = mapped_column(
        String(300), nullable=True
    )
    concluida: Mapped[bool] = mapped_column(
        Boolean, default=False
    )