
from fastapi import APIRouter
from app.schemas.url_schemas import URLRequest , URLResponse


router = APIRouter()

@router.get("/")
def home():
    return {
        "message":"Happy Learning!"
    }

@router.get("/health")
def check():
    return {
        "message":"system is healthy!"
    }
    
@router.post("/shorten",response_model = URLResponse)
def shorten_url(data : URLRequest):
    return {
        "short_url":"abc123",
        "original_url": str(data.url),
        "created":True
    }
    

