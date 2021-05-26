from starlette.testclient import TestClient

from app.core.dependencies import create_contracts_service
from app.main import app
from tests import TESTING_URL, configure_service_for_test

client = TestClient(app)


def test_handlers_generate_contract_success():
    url = f'{TESTING_URL}/?name=validName&company=Company'
    response = client.get(url)
    app.dependency_overrides[
        create_contracts_service] = configure_service_for_test

    assert response.status_code == 200


def test_handlers_generate_contract_failure_invalid_name_param():
    url = f'{TESTING_URL}/?name=sh&company=Company'
    response = client.get(url)
    app.dependency_overrides[
        create_contracts_service] = configure_service_for_test
    assert response.status_code == 422


def test_handlers_generate_contract_failure_invalid_company_param():
    url = f'{TESTING_URL}/?name=validName&company=c'
    response = client.get(url)
    app.dependency_overrides[
        create_contracts_service] = configure_service_for_test
    assert response.status_code == 422
