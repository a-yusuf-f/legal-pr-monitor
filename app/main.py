from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.article import Article
from app.database import engine, Base, get_db
from app.models.journalist import Journalist
from app.schemas.journalist import JournalistCreate
from app.models.tracked_keyword import TrackedKeyword
from app.schemas.tracked_keyword import TrackedKeywordCreate

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Legal PR Monitoring API"}

@app.post("/journalists")
def create_journalist(
    journalist: JournalistCreate,
    db: Session = Depends(get_db)
):
    existing_journalist = (
        db.query(Journalist)
        .filter(Journalist.email == journalist.email)
        .first()
    )

    if existing_journalist:
        raise HTTPException(
            status_code=400,
            detail="Journalist with this email already exists"
        )

    db_journalist = Journalist(
        name=journalist.name,
        publication=journalist.publication,
        email=journalist.email,
        topic=journalist.topic
    )

    db.add(db_journalist)
    db.commit()
    db.refresh(db_journalist)

    return db_journalist

@app.get("/journalists")
def get_journalists(db: Session = Depends(get_db)):
    return db.query(Journalist).all()

@app.get("/articles")
def get_articles(db: Session = Depends(get_db)):
    return db.query(Article).all()
@app.post("/keywords")
def create_keyword(
    keyword: TrackedKeywordCreate,
    db: Session = Depends(get_db)
):
    existing = (
        db.query(TrackedKeyword)
        .filter(TrackedKeyword.keyword == keyword.keyword)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Keyword already exists"
        )

    new_keyword = TrackedKeyword(
        keyword=keyword.keyword
    )

    db.add(new_keyword)
    db.commit()
    db.refresh(new_keyword)

    return new_keyword


@app.get("/keywords")
def get_keywords(
    db: Session = Depends(get_db)
):
    return db.query(TrackedKeyword).all()
