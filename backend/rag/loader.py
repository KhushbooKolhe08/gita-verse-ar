import os
from pypdf import PdfReader


def load_text_file(file_path):
    """Load plain text file"""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_pdf_file(file_path):
    """Extract text from PDF"""
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        try:
            text += page.extract_text() + "\n"
        except:
            pass  # skip problematic pages

    return text


def load_gita_data():
    """Main loader function"""
    
    base_path = os.path.dirname(os.path.dirname(__file__))
    
    txt_path = os.path.join(base_path, "data", "processed", "gita.txt")
    pdf_path = os.path.join(base_path, "data", "raw", "bgita.pdf")

    # Prefer TXT if exists (cleaner)
    if os.path.exists(txt_path):
        print("Loading from TXT...")
        return load_text_file(txt_path)

    elif os.path.exists(pdf_path):
        print("Loading from PDF...")
        return load_pdf_file(pdf_path)

    else:
        raise FileNotFoundError("No Gita file found in data folder.")