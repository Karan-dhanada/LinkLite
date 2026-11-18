import os
from dotenv import load_dotenv
from sqlalchemy import text , URL
from app.database import engine

load_dotenv()

DATABASE_URL = URL.create(
    drivername = "postgresql+psycopg",
    username = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    host = os.getenv("DB_HOST"),
    port = os.getenv("DB_PORT"),
    database = os.getenv("DB_NAME")    
)

print("USER:", os.getenv("DB_USER"))
print("PASSWORD:", os.getenv("DB_PASSWORD"))
print("HOST:", os.getenv("DB_HOST"))
print("PORT:", os.getenv("DB_PORT"))
print("DATABASE:", os.getenv("DB_NAME"))

print(DATABASE_URL.render_as_string(hide_password=True))
    