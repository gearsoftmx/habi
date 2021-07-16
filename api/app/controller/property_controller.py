from fastapi import APIRouter, Depends

from app.model.property_model import PropertyRequestModel
from app.service.property_service import PropertyService


# Aquí se define el api que el cliente consumirá
router = APIRouter(
    prefix='/properties',
)


@router.get('/', tags=['Properties'])
async def get_property(info: PropertyRequestModel = Depends(), service: PropertyService = Depends(PropertyService)):
    return service.get_properties(info)
