
from app.database import Base , engine
from app.models.url import URL

Base.metadata.create_all(bind=engine)