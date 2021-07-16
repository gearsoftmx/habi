import datetime
from typing import List

from pydantic import BaseModel


class ResponseModel(BaseModel):
    success: bool = False
    message: str = ''
    date: datetime.datetime = datetime.datetime.now()
    data: List = []
