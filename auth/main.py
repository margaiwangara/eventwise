from fastapi import FastAPI
from routers import auth
from models import user
from database import engine

app = FastAPI()

# Base user model
user.Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/api")


@app.get("/")
def hello_world():
    return {"message": "Hello World!"}
