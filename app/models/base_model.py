from sqlalchemy import Boolean, Column, DateTime, Integer

from app.core.db import Base


class BaseModel(Base):
    full_amount = Column(Integer)
    invested_amount = Column(Integer)
    fully_invested = Column(Boolean)
    create_date = Column(DateTime)
    close_date = Column(DateTime)
