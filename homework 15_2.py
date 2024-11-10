from fastapi import FastAPI
import uvicorn

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
def create_user(username: str, age: int) -> dict:
    new_user_id = str(int(max(users.keys(), default='0')) + 1)
    users[new_user_id] = f'Имя: {username}, возраст: {age}'
    return {"message": f"User {new_user_id} is registered"}


@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: str, username: str, age: int) -> dict:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return {"message": f"The user {user_id} is updated"}


@app.delete("/user/{user_id}")
def delete_user(user_id: str) -> dict:
    del users[user_id]
    return {"message": f"The user {user_id} is deleted"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)