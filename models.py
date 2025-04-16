from sqlalchemy import Column, Integer, String, DateTime, func, Text
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(Text, nullable=False)
    short_code = Column(Text, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime(timezone=True))
    access_count = Column(Integer, default=0, nullable=False)