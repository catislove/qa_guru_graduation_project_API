import allure
import jsonschema
from allure_commons.types import Severity

import conftest

service = "petstore"


@allure.feature('Ресурс "STORE"')
@allure.label('owner', 'Amalia')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.title('Создание заказа')
def test_post_store_order():
    schema = conftest.response_schema(conftest.read_json_schema('post_store_order.json'))
    payload = {
          "id": 10,
          "petId": 123,
          "quantity": 1,
          "shipDate": "2023-12-01T12:50:19.857Z",
          "status": "placed",
          "complete": "true"
    }

    response = conftest.api_request(
        service, "post",
        url="/store/order",
        json=payload
    )
    assert response.status_code == 200
    jsonschema.validators.validate(instance=response.json(), schema=schema)
    assert response.json()['id'] == payload['id']
    assert response.json()['petId'] == payload['petId']


@allure.feature('Ресурс "STORE"')
@allure.label('owner', 'Amalia')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.title('Получение данных о заказе по идентификатору')
def test_get_order_by_orderid():
    order_id = 2
    schema = conftest.response_schema(conftest.read_json_schema('get_order_by_orderid.json'))

    response = conftest.api_request(
        service, "get",
        url = f"/store/order/{order_id}"
    )

    jsonschema.validators.validate(instance=response.json(), schema=schema)
    assert response.status_code == 200

@allure.feature('Ресурс "STORE"')
@allure.label('owner', 'Amalia')
@allure.tag('api')
@allure.severity(Severity.NORMAL)
@allure.title('Удаление заказа по идентификатору')
def test_delete_order_by_orderid():
    order_id = 10
    schema = conftest.response_schema(conftest.read_json_schema('delete_order_by_orderid.json'))

    response = conftest.api_request(
        service, "delete",
        url = f"/store/order/{order_id}"
    )

    jsonschema.validators.validate(instance=response.json(), schema=schema)
    assert response.status_code == 200


