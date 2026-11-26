from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.url_routes import router
from app.database import Base, engine
from app.models.url import URL

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://link-lite-psi.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(router, prefix="/api")