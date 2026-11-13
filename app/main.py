
from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def home():
    return {"message":" Welcome !"}

@app.get("/health")
def health():
    return {"status":" Healthy ! "}

@app.get("/about")
def about():
    return {"Project Name":"LinkLite","Description":"A URL shortener app.."}

