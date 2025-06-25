#fastapi
from fastapi import FastAPI

from . import models
from .database import engine

#routers
from .routers import posts,users,auth,vote

from .config import settings

from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine) (we have alembic so no needed)

app = FastAPI()

origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():
    return{"message":"Hello"}

app.include_router(posts.router)

app.include_router(users.router)

app.include_router(auth.router)

app.include_router(vote.router)
