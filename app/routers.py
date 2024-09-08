from fastapi import APIRouter
from app.users.urls import userRouter
from app.tasks.urls import *


api_router = APIRouter()


api_router.include_router(userRouter, prefix='/users', tags=['API for USERS'])
api_router.include_router(taskRouter, prefix='/tasks', tags=['API for TASKS'])