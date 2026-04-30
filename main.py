from fastapi import FastAPI

from database import engine, Base
from routers import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)


@app.get("/")
def home():
    return {"mensagem": "API funcionando"}