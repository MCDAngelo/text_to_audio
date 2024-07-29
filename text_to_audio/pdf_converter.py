import re

from pypdf import PdfReader


class PDFConverter:
    def __init__(self, filename):
        self.reader = PdfReader(filename)
        self.pages = self.reader.pages

    def extract_all_text(self):
        self.raw_text = [page.extract_text() for page in self.pages]

    def clean_text(self):
        def _remove_page_num(x):
            return re.sub(r"^\s\d+\s", "", x)

        self.clean_pages = [_remove_page_num(raw) for raw in self.raw_text]
