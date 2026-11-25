
from fastapi import FastAPI , HTTPException
from app.routes.url_routes import router
from fastapi.middleware.cors import CORSMiddleware # for CORS middleware 

from app.database import Base, engine
from app.models.url import URL

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(router,prefix="/api")




app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






