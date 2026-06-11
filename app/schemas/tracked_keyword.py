from pydantic import BaseModel


class TrackedKeywordCreate(BaseModel):
    keyword: str
