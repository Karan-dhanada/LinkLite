
from fastapi import FastAPI , HTTPException
from app.routes.url_routes import router
from fastapi.middleware.cors import CORSMiddleware # for CORS middleware 

from app.database import Base, engine
from app.models.url import URL

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(router)




app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","https://link-lite-psi.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






