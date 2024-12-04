"""CRUD операции для модели Task"""
from datetime import datetime

from sqlalchemy import select, update

from src.db.models.task import Task, Status
from src.db.schemas.task import TaskAddDTO
from src.db.session import async_session_factory


async def add_task(new_task: TaskAddDTO):
    async with async_session_factory() as session:
        task = Task(**new_task.model_dump())
        session.add(task)
        await session.commit()
        await session.refresh(task)
        return task.id


async def select_task_by_id(id_task: int):
    async with async_session_factory() as session:
        query = select(Task).where(Task.id == id_task)
        result = await session.execute(query)
        result_on_print = result.mappings().first()
        return result_on_print


async def select_task_not_complete():
    async with async_session_factory() as session:
        query = select(Task).where(Task.status == Status.in_queue)
        result = await session.execute(query)
        result_on_print = result.mappings().all()
        if result_on_print:
            return result_on_print
        else:
            return []


async def update_task_time(id_task: int, type_time: str):
    async with async_session_factory() as session:
        if type_time == "start_time":
            stmt = update(Task).where(Task.id == id_task).values(status=Status.run, start_time=datetime.now())
        elif type_time == "exec_time":
            stmt = update(Task).where(Task.id == id_task).values(status=Status.completed, exec_time=datetime.now())
        await session.execute(stmt)
        await session.commit()
