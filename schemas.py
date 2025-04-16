from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

class URLCreate(BaseModel):
    url: HttpUrl

class URLUpdate(BaseModel):
    url: HttpUrl

class URLInfo(BaseModel):
    id: int
    url: HttpUrl
    short_code: str
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class URLStats(URLInfo):
    access_count: int