import sys
import os

sys.path.append(os.getcwd())

import feedparser

from app.database import SessionLocal
from app.models.article import Article
from app.models.tracked_keyword import TrackedKeyword
from app.models.article_match import ArticleMatch

RSS_FEED = "https://feeds.bbci.co.uk/news/rss.xml"

def run():
    db = SessionLocal()

    feed = feedparser.parse(RSS_FEED)

    keywords = db.query(TrackedKeyword).all()

    for entry in feed.entries[:5]:

        existing_article = (
            db.query(Article)
            .filter(Article.link == entry.link)
            .first()
        )

        if existing_article:
            article = existing_article
        else:
            article = Article(
                title=entry.title,
                link=entry.link,
                source="BBC News"
            )

            db.add(article)
            db.flush()

        for keyword in keywords:

            if keyword.keyword.lower() in article.title.lower():

                existing_match = (
                    db.query(ArticleMatch)
                    .filter(
                        ArticleMatch.article_id == article.id,
                        ArticleMatch.keyword_id == keyword.id
                    )
                    .first()
                )

                if existing_match:
                    continue

                match = ArticleMatch(
                    article_id=article.id,
                    keyword_id=keyword.id
                )

                db.add(match)

    db.commit()
    db.close()

    print("RSS ingestion complete")


if __name__ == "__main__":
    run()


if __name__ == "__main__":
    run()
