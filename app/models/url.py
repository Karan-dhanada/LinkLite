
from sqlalchemy import Column , Integer , String
from app.database import Base


class URL(Base):
    __tablename__ = "urls"
    
    id = Column(Integer,primary_key = True)
    short_code = Column(String,unique = True,nullable = False)
    original_url = Column(String, nullable = False)
    
