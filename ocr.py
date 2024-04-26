import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from docx import Document

pdf_path = 'pnu.pdf'
word_path = 'output.docx'


def pdf_to_png(pdf_path):
    # Open the PDF file
    pdf = fitz.open(pdf_path)

    # Iterate over PDF pages and convert each to PNG
    for page_num in range(len(pdf)):
        page = pdf[page_num]
        pix = page.get_pixmap()
        output = f'page_{page_num}.png'
        pix.save(output)
        yield output


def ocr_png_to_word(png_paths, word_path):
    # Create a new Word document
    doc = Document()

    # Iterate over PNG images and perform OCR
    with open("index.html", 'w+b') as f:
        for png_path in png_paths:
            text = pytesseract.image_to_pdf_or_hocr(
                Image.open(png_path), extension='hocr', lang="eng+equ")
            print(text)
            f.write(text)


# Convert PDF to PNG
ocr_png_to_word(list(pdf_to_png(pdf_path)), word_path)
