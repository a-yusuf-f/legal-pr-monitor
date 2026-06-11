from sqlalchemy import Column, Integer, String
from app.database import Base

class Journalist(Base):
    __tablename__ = "journalists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    publication = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    topic = Column(String)
