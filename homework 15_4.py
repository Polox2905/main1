from fastapi import FastAPI, Request, HTTPException, TemplateResponse
from pydantic import BaseModel
import uvicorn
from starlette.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
async def get_main_page(request: Request):
    context = {"request": request, "users": users}
    return templates.TemplateResponse("users.html", context)


@app.get("/user/{user_id}")
async def get_users(request: Request, user_id: int):
    try:
        user = next(u for u in users if u.id == user_id)
    except StopIteration:
        raise HTTPException(status_code=404, detail="User was not found")

    context = {"request": request, "user": user}
    return templates.TemplateResponse("users.html", context)


@app.post("/user/{username}/{age}")
def create_user(username: str, age: int):
    next_id = len(users) + 1
    new_user = User(id=next_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/update/{username}/{age}")
def update_user(user_id: int, username: str, age: int):
    index = next((i for i, u in enumerate(users) if u.id == user_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="User was not found")
    users[index].username = username
    users[index].age = age
    return users[index]


@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    index = next((i for i, u in enumerate(users) if u.id == user_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="User was not found")
    deleted_user = users.pop(index)
    return deleted_user


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)