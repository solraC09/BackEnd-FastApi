from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Task
from schemas import TasksCreate, TasksResponse

router = APIRouter()

@router.post("/tasks", response_model=TasksResponse)
def criar_tasks(tasks: TasksCreate, db: Session = Depends(get_db)):
    new_tasks = Task(
        titulo=tasks.titulo,
        descricao=tasks.descricao
    )

    db.add(new_tasks)
    db.commit()
    db.refresh(new_tasks)

    return new_tasks


@router.get("/tasks", response_model=list[TasksResponse])
def listar_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()


@router.get("/tasks/{tasks_id}")
def buscar_tasks(tasks_id: int, db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(Task.id == tasks_id).first()

    if tasks:
        return tasks

    return {"message": "Task not found"}


@router.put("/tasks/{tasks_id}")
def atualizar_tasks(tasks_id: int, dados: TasksCreate, db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(Task.id == tasks_id).first()

    if tasks:
        tasks.titulo = dados.titulo
        tasks.descricao = dados.descricao

        db.commit()
        db.refresh(tasks)

        return tasks

    return {"message": "Task not found"}

@router.patch("/tasks/{task_id}/concluir")
def concluir_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task:
        task.concluida = True
        db.commit()

        return {"message": "Task completed"}
    
    return {"message": "Task not found"}


@router.delete("/tasks/{tasks_id}")
def deletar_tasks(tasks_id: int, db: Session = Depends(get_db)):
    tasks = db.query(Task).filter(Task.id == tasks_id).first()

    if tasks:
        db.delete(tasks)
        db.commit()

        return {"message": "Task deleted successfully"}

    return {"message": "Task not found"}