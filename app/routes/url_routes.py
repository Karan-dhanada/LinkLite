
import secrets
from fastapi import APIRouter , Depends , HTTPException
from app.schemas.url_schemas import URLRequest , URLResponse
from app.database import get_db 
from app.models.url import URL
from sqlalchemy.orm import Session


   
router = APIRouter()


@router.post("/shorten",response_model = URLResponse)
def shorten_url(data : URLRequest , db:Session = Depends(get_db)):
    
    short_code = secrets.token_urlsafe(6)
    
    new_url = URL( short_code = short_code , original_url = str(data.url))
    
    db.add(new_url)
    db.commit()
    
    return {
        "short_url":new_url.short_code,
        "original_url":new_url.original_url,
        "created":True
    }
    

    
    

