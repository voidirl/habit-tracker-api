from fastapi import FastAPI

from app.db.session import Base, engine
from app import models 
from app.routers.routers import router as auth_router
app = FastAPI(title="HabitTracker API")

app.include_router(auth_router)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "ok"}