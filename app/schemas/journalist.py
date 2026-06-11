from pydantic import BaseModel

class JournalistCreate(BaseModel):
    name: str
    publication: str
    email: str
    topic: str
