from tortoise import Tortoise, fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class Module(Model):
    id: int
    title = fields.CharField(25)

    # Связь "Один ко многим" с уровнем
    levels = fields.ReverseRelation["Level"]

Tortoise.init_models(["app.tasks.models"], "models")
GetModule = pydantic_model_creator(Module, name="Module")
CreateModule = pydantic_model_creator(Module, name="ModuleIn", exclude_readonly=True)


class Level(Model):
    id = fields.IntField(pk=True)
    module = fields.ForeignKeyField(
        "models.Module", related_name="levels")
    title = fields.CharField(50)

    # task = fields.ForeignKeyRelation[Task] = fields.ForeignKeyField(
    #     "models.Task", related_name="tasks")

    tasks = fields.ReverseRelation["Task"]


Tortoise.init_models(["app.tasks.models"], "models")
GetLevel = pydantic_model_creator(Level, name="Level")
CreateLevel = pydantic_model_creator(Level, name="LevelIn", exclude_readonly=True)



class Task(Model):
    id = fields.IntField(pk=True)
    level = fields.ForeignKeyField("models.Level", related_name="tasks")
    question = fields.TextField()
    answer = fields.JSONField(null=True)
    key = fields.IntField()


Tortoise.init_models(["app.tasks.models"], "models")
GetTask = pydantic_model_creator(Task, name="Task",)
CreateTask = pydantic_model_creator(Task, name="TaskIn", exclude_readonly=True, exclude=['answer'])



