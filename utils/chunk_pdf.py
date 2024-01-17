

import PyPDF2


path = "data/week6_data.pdf"

def read_pdf(path):
    # Open the PDF file in binary read mode
    text = ""
    with open(path, "rb") as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page in range(num_pages):
            page_obj = pdf_reader.pages[page]
            extracted_text = page_obj.extract_text()
            text += extracted_text

    print(text)

    return text

