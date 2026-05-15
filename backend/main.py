from fastapi import FastAPI

app = FastApi(tittle="Blog", version="0.1.0")

@app.get("/")
def hello():
    return {"msg": "Hello FastApi"}