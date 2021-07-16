from sqlalchemy import Column, Integer, DATETIME, ForeignKey
from sqlalchemy.orm import relationship
from app.library.database.mysql.sql_alchemy_base import base


class StatusHistoryModel(base):
    __tablename__ = "status_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    property_id = Column(Integer, ForeignKey("property.id"))
    status_id = Column(Integer, ForeignKey('status.id'))
    update_date = Column(DATETIME)
    properties = relationship('PropertyModel', back_populates="status_history")
