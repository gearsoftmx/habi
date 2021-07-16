from enum import Enum


class StatusVisibleUserEnum(Enum):
    PRE_VENTA = 3
    EN_VENTA = 4
    VENDIDO = 5

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class StatusEnum(Enum):
    COMPRANDO = 1
    COMPRADO = 2

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_