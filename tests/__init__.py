import os

from app.external.google_docs import GoogleDocsAPIMock
from app.services.contracts import ContractService
from app.utils.pdf import PDFCreatorImpl

TEST_FILE_DIR = "test"

TESTING_URL = "api/contracts/generate-contract"


def configure_service_for_test() -> ContractService:
    google_docs = GoogleDocsAPIMock()
    pdf_creator = PDFCreatorImpl()

    if not os.path.exists(TEST_FILE_DIR):
        os.makedirs(TEST_FILE_DIR)

    return ContractService(files_path=TEST_FILE_DIR, google_docs=google_docs,
                           pdf_creator=pdf_creator)
