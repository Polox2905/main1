from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Главная страница"}

@app.get("/user/admin")
def admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
def user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/")
def user_info(username: str = "Paul", age: int = 40):
    return {
        "message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)