from sqlalchemy import Column, Integer, String
from app.database import Base


class TrackedKeyword(Base):
    __tablename__ = "tracked_keywords"

    id = Column(Integer, primary_key=True, index=True)
    keyword = Column(String, unique=True, nullable=False)
