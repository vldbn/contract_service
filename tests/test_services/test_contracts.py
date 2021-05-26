from tests import configure_service_for_test


def test_contract_service_generate_contract_success():
    contract_service = configure_service_for_test()
    file_path = contract_service.generate_contract(name="test name",
                                                   company="test company")

    assert file_path

# Also it will be useful to extend GoogleDocsAPIMock class with simulating
# connection errors and file not find errors and to test service class:

# def test_contract_service_generate_contract_failure_connection_err():
#   test behavior of service class, when Google Docs services are not
#   available

# def test_contract_service_generate_contract_failure_no_file_err():
#   test behavior of service class, when templates file doesn't exists
#   in Google Docs
