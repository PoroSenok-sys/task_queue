"""Файл для имитации выполнения Tasks"""
import asyncio
import random

from src.repositories.task_repositories import select_task_not_complete, update_task_time


async def completing_tasks():
    """Функция для выполнения задач"""
    semaphore = asyncio.Semaphore(2)

    async def prepare_and_process(task):
        async with semaphore:
            await process_task(task)

    while True:
        tasks = await select_task_not_complete()
        if tasks:
            await asyncio.gather(*(prepare_and_process(task["Task"]) for task in tasks))
        else:
            await asyncio.sleep(10)


async def process_task(task):
    """Функция, которая имитирует выполнение задачи"""
    await update_task_time(task.id, "start_time")
    await asyncio.sleep(random.randint(1, 10))
    await update_task_time(task.id, "exec_time")
