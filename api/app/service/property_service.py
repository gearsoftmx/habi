from fastapi import Depends

from app.repository.property_repository import PropertyRepository
from app.enum.status_enum import StatusVisibleUserEnum
from app.model.property_model import PropertyResponseModel
from app.model.response_model import ResponseModel


# Clase encargada de procesar la información que envía el repository para colocarla en un modelo de respuesta pydantic
class PropertyService:

    def __init__(self, repository: PropertyRepository = Depends(PropertyRepository)):
        self.repository = repository
        self.response = ResponseModel()

    def get_properties(self, info):
        if info.status_id == 0 or StatusVisibleUserEnum.has_value(info.status_id):
            result = self.repository.consult_properties(info)
            if result is not None and result != '' and len(result) > 0:
                for row in result:
                    property_response = PropertyResponseModel()
                    property_response.address = row[0].properties.address
                    property_response.city = row[0].properties.city
                    property_response.state = row[1]
                    property_response.price = row[0].properties.price
                    property_response.description = '' if row[0].properties.description is None else row[0].properties.description
                    self.response.data.append(property_response)
            self.response.success = True
            self.response.message = 'success'
            return self.response
        else:
            self.response.success = False
            self.response.message = 'There are no results for this consult'
            return self.response
