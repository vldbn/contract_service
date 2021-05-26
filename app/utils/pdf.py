from abc import ABC, abstractmethod

from fpdf import FPDF


class PDFCreator(ABC):
    """Abstract class for PDF Creator"""

    @abstractmethod
    def create_pdf(self, folder_path: str, text: str) -> str:
        raise NotImplementedError


class PDFCreatorImpl(PDFCreator):
    """Class implements methods of PDFCreator abstract class."""

    def __init__(self):
        self.pdf = FPDF("P", "mm", "A4")

    def create_pdf(self, folder_path: str, text: str) -> str:
        """Creates and save PDF file from text."""

        file_path = f'{folder_path}/contract.pdf'

        if len(self.pdf.pages) == 0:
            self.pdf.add_page()

        # Set font: Times, normal, size 10
        self.pdf.set_font('Times', '', 16)
        self.pdf.cell(0, 10, txt=text)
        self.pdf.output(file_path, "F")

        return file_path
