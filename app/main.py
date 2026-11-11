from fastapi import FastAPI

from app.calculator import add, multiply, subtract

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Application is running!"}


@app.get("/add/{a}/{b}")
def addition(a: int, b: int):
    return {"result": add(a, b)}


@app.get("/subtract/{a}/{b}")
def subtraction(a: int, b: int):
    return {"result": subtract(a, b)}


@app.get("/multiply/{a}/{b}")
def multiplication(a: int, b: int):
    return {"result": multiply(a, b)}