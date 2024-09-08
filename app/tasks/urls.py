from typing import List, Optional
from fastapi import APIRouter, HTTPException, Depends, Response
from fastapi.responses import JSONResponse
from .models import *

taskRouter = APIRouter()



#Module
@taskRouter.post('/module', response_model=CreateModule, name="Создание модуля")
async def create_module(object_: CreateModule):  #type: ignore
    module_obj = await Module.create(title=object_.title)
    return await GetModule.from_tortoise_orm(module_obj)


@taskRouter.get('/module/all', response_model=List[GetModule], name="Получение всех модулей")
async def get_all_modules():
    return await GetModule.from_queryset(Module.all())



#Level
@taskRouter.post('/level', response_model=CreateLevel, name="Создание уровня")
async def create_level(level: CreateLevel): #type: ignore
    module = await Module.get(id=level.module_id) 
    level_obj = await Level.create(title=level.title,
                                   module_id=level.module_id)
    
    return JSONResponse(content={"id":level_obj.id,
                                 "title":level_obj.title,
                                 "module":module.title})


@taskRouter.get('/level/all', response_model=List[GetLevel], description="---", name="Получение всех уровней")
async def all_list():
    return await GetLevel.from_queryset(Level.all())

