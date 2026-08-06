import pdfplumber
from docx import Document


def extract_pdf_text(file_path: str) -> str:
    """Extract text from a PDF file."""

    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def extract_docx_text(file_path: str) -> str:
    """Extract text from a DOCX file."""

    document = Document(file_path)

    text = ""

    for para in document.paragraphs:
        text += para.text + "\n"

    return text


def extract_resume_text(file_path: str) -> str:
    """Detect file type and extract text."""

    if file_path.endswith(".pdf"):
        return extract_pdf_text(file_path)

    elif file_path.endswith(".docx"):
        return extract_docx_text(file_path)

    else:
        raise ValueError("Unsupported file format")