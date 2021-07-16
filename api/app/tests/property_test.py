from fastapi.testclient import TestClient

from app.main import app
from app.json import property_test_json

client = TestClient(app)


# Test para validar cuando se aplican 3 filtros
def test_1_get_properties():
    response = client.get("/properties/?status_id=3&city=medellin&year=2011").json()
    assert response['success'] == True
    assert response['data'] == property_test_json.TEST_1


# Test para validar cuando no se aplica ningun filtro
def test_2_get_properties():
    response = client.get("/properties/").json()
    assert response['success'] == True
    assert response['data'] == property_test_json.TEST_2


# Test para validar cuando se aplican 2 filtros
def test_3_get_properties():
    response = client.get("/properties/?status_id=3&city=medellin").json()
    assert response['success'] == True
    assert response['data'] == property_test_json.TEST_3


# Test para validar cuando se aplica un status id fuera de los permitidos que puede consultar el usuario (1 y 2)
def test_4_get_properties():
    response = client.get("/properties/?status_id=1").json()
    assert response['success'] == False
