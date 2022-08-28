from fastapi import FastAPI

app = FastAPI()

@app.get("/isum/")
def sum(a: int, b: int):
    return {"result": a+b}

@app.get("/isub/")
def sum(a: int, b: int):
    return {"result": a-b}

@app.get("/imul/")
def sum(a: int, b: int):
    return {"result": a*b}

@app.get("/idiv/")
def sum(a: int, b: int):
    return {"result": int(a/b)}