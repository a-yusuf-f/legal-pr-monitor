from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base


class ArticleMatch(Base):
    __tablename__ = "article_matches"

    id = Column(Integer, primary_key=True, index=True)

    article_id = Column(
        Integer,
        ForeignKey("articles.id"),
        nullable=False
    )

    keyword_id = Column(
        Integer,
        ForeignKey("tracked_keywords.id"),
        nullable=False
    )
