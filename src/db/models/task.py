"""Файл модели Task"""
from sqlalchemy.orm import Mapped, mapped_column

from enum import Enum
from datetime import datetime

from src.db.session import Base


class Status(str, Enum):
    in_queue = "In Queue"
    run = "Run"
    completed = "Completed"


class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[Status] = mapped_column(default=Status.in_queue)
    create_time: Mapped[datetime] = mapped_column(default=datetime.now())
    start_time: Mapped[datetime] = mapped_column(nullable=True)
    exec_time: Mapped[datetime] = mapped_column(nullable=True)
