
import secrets
from fastapi import APIRouter , Depends , HTTPException
from app.schemas.url_schemas import URLRequest , URLResponse
from app.database import get_db 
from app.models.url import URL
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

   
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

@router.get("/urls",response_model = list[URLResponse])
def  get_url(db:Session = Depends(get_db)):
    
    urls = db.query(URL).all()
    
    return [
        
        {
            "short_url":url.short_code,
            "original_url":url.original_url,
            "created":True
        }
        for url in urls
    ]

@router.get("/search/{short_code}")
def search_url(short_code:str , db:Session = Depends(get_db)):
    
    url = db.query(URL).filter(
        URL.short_code == short_code
    ).first()
    
    if url is None:
     raise HTTPException(status_code=404, detail="URL not found")
    
    return RedirectResponse(
        url  = url.original_url,
        status_code = 307
    )

    
    

