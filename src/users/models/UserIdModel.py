from pydantic import BaseModel


class UserIdModel(BaseModel):
    username: str
    password: str
    search_id: str
