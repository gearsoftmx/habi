from sqlalchemy import BIGINT, Column, Integer, String
from sqlalchemy.orm import relationship

from pydantic import BaseModel
from typing import Optional

from app.library.database.mysql.sql_alchemy_base import base


class PropertyModel(base):
    __tablename__ = "property"

    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String)
    city = Column(String)
    price = Column(BIGINT)
    description = Column(String)
    year = Column(Integer)
    status_history = relationship('StatusHistoryModel', back_populates="properties")


class PropertyRequestModel(BaseModel):
    status_id: Optional[int] = 0
    city: Optional[str] = ''
    year: Optional[int] = 0


class PropertyResponseModel(BaseModel):
    address: str = ''
    city: str = ''
    state: str = ''
    price: str = ''
    description: str = ''
