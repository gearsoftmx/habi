from sqlalchemy import Column, Integer, String

from app.library.database.mysql.sql_alchemy_base import base


class ILikeUsersModel(base):
    __tablename__ = "i_like_users"

    idi_like_users = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer)
    i_property = Column(String)
    date = Column(String)
