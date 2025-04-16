from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db_conn import create_db
from schemas import URLCreate, URLUpdate, URLInfo, URLStats
from fastapi.middleware.cors import CORSMiddleware
from crud import create_short_url, get_url_by_code, increment_access_count, update_url, delete_url, get_url_stats
import models
import uvicorn, os
from sqlalchemy.orm import Session

engine, SessionLocal = create_db()
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener Service")

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

origins = [
    "*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shorten", response_model=URLInfo)
def shorten_url(payload: URLCreate, db: Session = Depends(get_db)):
    return create_short_url(db, original_url=str(payload.url))

@app.get("/shorten/{code}", response_model=URLInfo)
def retrieve_url(short_code: str, db: Session = Depends(get_db)):
    url_obj = get_url_by_code(db, short_code)
    if not url_obj:
        raise HTTPException(status_code=404, detail="Short URL not found")
    increment_access_count(db, url_obj)
    return url_obj

# 3. Update short URL
@app.put("/shorten/{code}", response_model=URLInfo)
def update_shortened_url(short_code: str, payload: URLUpdate, db: Session = Depends(get_db)):
    url_obj = update_url(db, short_code, str(payload.url))
    if not url_obj:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return url_obj

@app.delete("/shorten/{code}", status_code=204)
def delete_shortened_url(short_code: str, db: Session = Depends(get_db)):
    deleted = delete_url(db, short_code)
    if not deleted:
        raise HTTPException(status_code=404, detail="Short URL not found")

@app.get("/shorten/{code}/stats", response_model=URLStats)
def stats(short_code: str, db: Session = Depends(get_db)):
    url_obj = get_url_stats(db, short_code)
    if not url_obj:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return url_obj

if __name__ == "__main__":
    uvicorn.run("init:app", host=HOST, port=int(PORT), reload=True)