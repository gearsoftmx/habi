from fastapi import Depends
from sqlalchemy import or_, func

from app.model.property_model import PropertyModel
from app.model.status_history_model import StatusHistoryModel
from app.library.database.mysql.mysql import MYSQLConnection
from app.enum.status_enum import StatusVisibleUserEnum

# Clase encargada de obtener la info de base de datos
class PropertyRepository:

    def __init__(self, connection: MYSQLConnection = Depends(MYSQLConnection)):
        self.session = connection.get_session()

    def consult_properties(self, info):
        properties = self.session.query(StatusHistoryModel, func.max(StatusHistoryModel.status_id)
                                        ).join(PropertyModel)
        filters = []
        if info.status_id == 0:
            filters.append(or_(StatusHistoryModel.status_id == StatusVisibleUserEnum.PRE_VENTA.value,
                               StatusHistoryModel.status_id == StatusVisibleUserEnum.EN_VENTA.value,
                               StatusHistoryModel.status_id == StatusVisibleUserEnum.VENDIDO.value))
        elif info.status_id > 0 and StatusVisibleUserEnum.has_value(info.status_id):
            filters.append(StatusHistoryModel.status_id == info.status_id)
        if info.city != '':
            filters.append(PropertyModel.city == info.city)
        if info.year > 0:
            filters.append(PropertyModel.year == info.year)
        properties = properties.filter(StatusHistoryModel.status_id).filter(*filters).group_by(StatusHistoryModel.property_id)
        result = properties.all()
        return result
