from pydantic import BaseModel , HttpUrl

class URLResponse(BaseModel):
    short_url:str
    original_url:str
    created:bool

class URLRequest(BaseModel):
    url: HttpUrl
    