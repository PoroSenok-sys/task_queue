"""Файл Старта приложения"""
import asyncio
import os
import sys

from fastapi import FastAPI

from src.routers.queue import router as router_queue
from src.service.completing_task import completing_tasks

sys.path.insert(1, os.path.join(sys.path[0], '..'))

app = FastAPI(
    title="Сервис для работы с очередью"
)

app.include_router(router_queue)

# Запускаем обработчик задач при старте приложения
task = asyncio.create_task(completing_tasks())
