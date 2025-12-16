from fastapi import FastAPI
from app.routes import users

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(users.router)