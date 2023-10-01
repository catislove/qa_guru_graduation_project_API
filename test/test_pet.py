import allure
import jsonschema
import pytest
from allure_commons.types import Severity

import conftest

service = "petstore"


@allure.feature('Ресурс "PET"')
@allure.label('owner', 'Amalia')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.title('Добавление нового животного в магазин')
def test_post_add_new_pet_for_store():
    schema = conftest.response_schema(conftest.read_json_schema('post_add_new_pet_for_store.json'))
    payload = {
          "id": 123,
          "category": {
            "id": 1,
            "name": "test_pet"
          },
          "name": "test_pet",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 1,
              "name": "string"
            }
          ],
          "status": "available"
        }
    response = conftest.api_request(
        service, "post",
        url="/pet",
        json=payload
    )
    assert response.status_code == 200
    jsonschema.validators.validate(instance=response.json(), schema=schema)
    assert response.json()['id'] == payload['id']
    assert response.json()['name'] == payload['name']


@allure.feature('Ресурс "PET"')
@allure.label('owner', 'Amalia')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.title('Редактирование данных созданного животного')
def test_put_add_new_pet_for_store():
    schema = conftest.response_schema(conftest.read_json_schema('post_add_new_pet_for_store.json'))
    payload = {
          "id": 123,
          "category": {
            "id": 1,
            "name": "test_pet_edited"
          },
          "name": "test_pet_edited",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 1,
              "name": "string"
            }
          ],
          "status": "available"
        }
    response = conftest.api_request(
        service, "post",
        url="/pet",
        json=payload
    )
    assert response.status_code == 200
    jsonschema.validators.validate(instance=response.json(), schema=schema)
    assert response.json()['id'] == payload['id']
    assert response.json()['name'] == payload['name']


@allure.feature('Ресурс "PET"')
@allure.label('owner', 'Amalia')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.title('Получение данных о животном по его идентификатору')
def test_get_pet_by_id():
    petID = 123
    schema = conftest.response_schema(conftest.read_json_schema('get_pet_by_id.json'))

    response = conftest.api_request(
        service, "get",
        url=f"/pet/{petID}"
    )

    jsonschema.validators.validate(instance=response.json(), schema=schema)
    assert response.status_code == 200


@allure.feature('Ресурс "PET"')
@allure.label('owner', 'Amalia')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.title('Удаление животного по идентификатору')
def test_delete_pet_by_id():
    petID = 123
    schema = conftest.response_schema(conftest.read_json_schema('delete_pet_by_id.json'))

    response = conftest.api_request(
        service, "delete",
        url=f"/pet/{petID}"
    )

    jsonschema.validators.validate(instance=response.json(), schema=schema)
    assert response.status_code == 200