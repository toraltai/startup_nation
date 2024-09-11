import json
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


#Task
@taskRouter.post('/task', response_model=CreateTask, name="Создание задачи")
async def create_module(object_: CreateTask, #type: ignore
                        answer_1,
                        answer_2,
                        answer_3,):
    
    answer = {"Ответ 1":answer_1,
              "Ответ 2":answer_2,
              "Ответ 3":answer_3,}
    
    answers_json = json.dumps(answer)
    
    task_obj = await Task.create(level_id=object_.level_id,
                                 question=object_.question,
                                 answer = answers_json,
                                 key = object_.key
                                 )
    return JSONResponse(content={"id":task_obj.id,
                                 "question":task_obj.question,
                                 "answer":task_obj.answer,
                                 "correct_answer":task_obj.key})



@taskRouter.post('/task/{task_id}/check')
async def check_task(task_id: int, answer: int):
    task = await Task.get(id=task_id)
    if task.key == answer:
        return {"result": "Correct"}
    else:
        return {"result": "Incorrect"}


@taskRouter.get('/task/all', response_model=List[GetTask], description="---", name="Получение всех Задач")
async def all_list():
    return await GetTask.from_queryset(Task.all())


@taskRouter.get("/task/{id}", response_model=GetTask)
async def get_task(object_id: int):
    return await GetTask.from_queryset_single(Task.get(id=object_id))
