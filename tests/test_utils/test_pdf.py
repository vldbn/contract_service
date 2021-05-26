import os

from app.utils.pdf import PDFCreatorImpl
from tests import TEST_FILE_DIR


def test_pdf_creator():
    if not os.path.exists(TEST_FILE_DIR):
        os.makedirs(TEST_FILE_DIR)

    pdf_creator = PDFCreatorImpl()
    file_path = pdf_creator.create_pdf(TEST_FILE_DIR, "test text")
    assert len(os.listdir(TEST_FILE_DIR)) == 1

    os.remove(file_path)
    os.rmdir(TEST_FILE_DIR)
