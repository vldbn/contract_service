from app.core.config import Config
from app.external.google_docs import GoogleDocsAPIImpl
from app.services.contracts import ContractService
from app.utils.pdf import PDFCreatorImpl


def create_contracts_service() -> ContractService:
    conf = Config()
    google_docs = GoogleDocsAPIImpl()
    pdf_creator = PDFCreatorImpl()

    return ContractService(files_path=conf.files_path, google_docs=google_docs,
                           pdf_creator=pdf_creator)
