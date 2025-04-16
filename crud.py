from sqlalchemy.future import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from models import URL
from helpers import generate_short_code

def create_short_url(db: Session, original_url: str) -> URL:
    short_code = generate_short_code()
    while db.scalar(select(URL).where(URL.short_code == short_code)):
        short_code = generate_short_code()

    new_url = URL(url=original_url, short_code=short_code)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return new_url
