import os

from app.external.google_docs import GoogleDocsAPIMock
from tests import TEST_FILE_DIR


def test_google_docs_api_mock():
    if not os.path.exists(TEST_FILE_DIR):
        os.makedirs(TEST_FILE_DIR)
    google_docs = GoogleDocsAPIMock()
    google_docs.download_template(TEST_FILE_DIR)
    assert len(os.listdir(TEST_FILE_DIR)) == 1

    google_docs.delete_template(TEST_FILE_DIR)
    assert len(os.listdir(TEST_FILE_DIR)) == 0

    os.rmdir(TEST_FILE_DIR)

# Also it will be useful to extend GoogleDocsAPIMock class with simulating
# connection errors and file not find and test it:
# test_google_docs_api_mock_failure_connection_err()
# test_google_docs_api_mock_failure_no_file_err()
