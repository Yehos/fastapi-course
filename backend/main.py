from fastapi import FastAPI

app = FastAPI(tittle="Blog", version="0.1.0")

@app.get("/")
def hello():
    return {"msg": "Hello FastApi"}