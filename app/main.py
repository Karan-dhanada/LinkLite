
from fastapi import FastAPI 
from pydantic import BaseModel , HttpUrl

app = FastAPI()

class URLRequest(BaseModel):
    url : HttpUrl


@app.get("/")
def home():
    return {"message":" Welcome !"}

@app.get("/health")
def health():
    return {"status":" Healthy ! "}

@app.get("/about")
def about():
    return {"Project Name":"LinkLite","Description":"A URL shortener app.."}

@app.get("/users/{user_id}")
def get_user(user_id:int):
    return {
        "user_id":user_id,
        "message":"details fetched succesfully"
    }

@app.get("/users")
def get_student(user_name:str = "all"):
    if user_name == "all":
        return {"message":"All students displayed"}
    return {
        "search_name":user_name,
        "message":"search results are out"
    }

@app.post("/shorten")
def shorten_url(data : URLRequest):
    return {
        "original_url":str(data.url),
        "message":"URL received successfully"
    }
