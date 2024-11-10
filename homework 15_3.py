from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users", response_model=users)
async def get_users():
    return users


@app.post("/user/{username}/{age}", response_model=User)
def create_user(username: str, age: int):
    next_id = len(users) + 1
    new_user = User(id=next_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/update/{username}/{age}", response_model=User)
def update_user(user_id: int, username: str, age: int):
    index = next((i for i, u in enumerate(users) if u.id == user_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="User was not found")
    users[index].username = username
    users[index].age = age
    return users[index]


@app.delete("/user/{user_id}", response_model=User)
def delete_user(user_id: int):
    index = next((i for i, u in enumerate(users) if u.id == user_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="User was not found")
    deleted_user = users.pop(index)
    return deleted_user


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)