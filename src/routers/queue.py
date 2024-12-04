"""Файл с роутерами для работы с очередью"""
from fastapi import APIRouter, HTTPException

from src.db.schemas.task import TaskAddDTO
from src.repositories.task_repositories import add_task, select_task_by_id, select_task_not_complete

router = APIRouter(
    prefix="/queue",
    tags=["Working with a queue"]
)


@router.post("/")
async def post_task():
    new_task = TaskAddDTO()
    id_task = await add_task(new_task)
    return {
        "code": "200",
        "massage": f"Задача успешно добавлена, её номер - {id_task}"
    }


@router.get("/{id_task}")
async def get_task_by_id(id_task: int):
    task = await select_task_by_id(id_task)
    if task:
        return {
            "status_code": "200",
            "massage": f"Задача с номером {id_task} успешно найдена",
            "result": task["Task"]
        }
    else:
        raise HTTPException(
            status_code=400,
            detail="Задачи с указанным номером нет"
        )
