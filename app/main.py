
from fastapi import FastAPI , HTTPException
from app.routes.url_routes import router

app = FastAPI()

app.include_router(router,prefix="/api")








