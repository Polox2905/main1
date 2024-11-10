from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Главная страница"}

@app.get("/user/admin")
def admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
def user(
    user_id: Annotated[int, Path(gt=0, le=100, description="Enter User ID", example=1)]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
def user_info(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)],
):
    return {
        "message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)