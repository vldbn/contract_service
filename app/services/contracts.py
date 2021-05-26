import os

from app.external.google_docs import GoogleDocsAPI
from app.utils.pdf import PDFCreator


class ContractService:
    """Contract service class contains main logic of the application."""

    def __init__(self, files_path: str, google_docs: GoogleDocsAPI,
                 pdf_creator: PDFCreator) -> None:
        self.files_path = files_path
        self.google_docs = google_docs
        self.pdf_creator = pdf_creator

    def __call__(self):
        return self

    def generate_contract(self, name: str, company: str) -> str:
        """
        Downloads contract template from Google Docs, replaces placeholders,
        saves result to PDF.
        """

        template_path = self.google_docs.download_template(self.files_path)

        with open(template_path) as f:
            template = f
            txt = "".join(template.readlines())
            # here we should implement logic for replacing place holders
            # in template
            pdf_path = self.pdf_creator.create_pdf(self.files_path, txt)

        self.google_docs.delete_template(self.files_path)
        return pdf_path

    def delete_contract(self, file_path) -> None:
        """Deletes saved contract."""

        try:
            os.remove(file_path)
        except FileNotFoundError:
            pass
