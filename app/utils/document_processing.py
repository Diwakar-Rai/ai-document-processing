import fitz 
import pytesseract

from PIL import Image 

def extract_text_from_pdf(file_path:str)->str:
    document = fitz.open(file_path)
    extracted_text = []

    for page in document:
        extracted_text.append(page.get_text())
    return "\n".join(extracted_text)

def extract_text_from_image(file_path: str)->str:
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    return text