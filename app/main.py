from fastapi import FastAPI

from app.db.session import Base, engine
from app import models 
app = FastAPI(title="HabitTracker API")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "ok"}