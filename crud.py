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

def get_url_by_code(db: Session, short_code: str) -> URL | None:
    return db.scalar(select(URL).where(URL.short_code == short_code))

def increment_access_count(db: Session, url_obj: URL):
    url_obj.access_count += 1
    db.commit()
    db.refresh(url_obj)

def update_url(db: Session, short_code: str, new_url: str) -> URL | None:
    url_obj = get_url_by_code(db, short_code)
    if url_obj:
        url_obj.url = new_url
        db.commit()
        db.refresh(url_obj)
        return url_obj
    return None

def delete_url(db: Session, short_code: str) -> bool:
    url_obj = get_url_by_code(db, short_code)
    if url_obj:
        db.delete(url_obj)
        db.commit()
        return True
    return False  

def get_url_stats(db: Session, short_code: str) -> URL | None:
    return get_url_by_code(db, short_code)