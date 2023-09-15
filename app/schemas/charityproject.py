from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field, validator, PositiveInt


class CharityProjectBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: PositiveInt
    invested_amount: PositiveInt = 0
    fully_invested: bool = False
    create_date: datetime = datetime.now()
    close_date: Optional[datetime]

    class Config:
        orm_mode = True


class CharityProjectCreate(CharityProjectBase):
    pass


class CharityProjectDB(CharityProjectBase):
    id: int


class CharityProjectUpdate(CharityProjectBase):

    @validator('name')
    def name_cant_be_null(cls, value: Optional[str]):
        if value is None:
            raise ValueError('Имя не может быть None|null')

        return value
