from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.library.database.mysql.sql_alchemy_base import base


class StatusModel(base):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    label = Column(String)
    status_history = relationship('StatusHistoryModel', back_populates="status")
