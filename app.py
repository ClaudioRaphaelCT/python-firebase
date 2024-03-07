from fastapi import FastAPI
from src.users.methods.read.controllers.getAllUsers import validate_user
from src.users.models.UserModel import UserModel
from src.users.methods.create.createUser import insert_user
from src.users.models.UserIdModel import UserIdModel
from src.users.methods.read.controllers.getUserID import get_user_by_id

app = FastAPI(title="Mock API")


@app.get("/")
def home():
    return {"swagger": "/docs"}


@app.post("/users/create")
def create_user(user: UserModel):
    return insert_user(user.username, user.password)


@app.get("/users")
def get_user(user: UserModel):
    return validate_user(user.username, user.password)


@app.get("/users/id")
def get_id(user: UserIdModel):
    return get_user_by_id(user.search_id, user.username, user.password)
