from fastapi import APIRouter
from app.users.urls import userRouter


api_router = APIRouter()


api_router.include_router(userRouter, prefix='/users', tags=['API for USERS'])