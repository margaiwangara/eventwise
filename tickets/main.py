from fastapi import FastAPI
from models import ticket
from database import engine
from routers import tickets

app = FastAPI()

app.include_router(tickets.router, prefix="/api")

# Base ticket model
ticket.Base.metadata.create_all(bind=engine)


@app.get("/")
def hello_world():
    return {"message": "Hello World!"}
