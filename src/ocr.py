import fitz
import pytesseract
from io import BytesIO
from PIL import Image
from logger import get_logger

LOGGER = get_logger()


def extract_text_from_pdf(pdf_binary: BytesIO, dpi=300) -> str:
    """
    Converts each page of a PDF file (provided as binary) into a text.

    Args:
        pdf_binary (bytes): The binary content of the PDF file.
        dpi (int): The DPI (Dots Per Inch) for rendering the images. Higher DPI
                   results in higher resolution images but larger file sizes.
                   Defaults to 300.
    """
    try:
        # Open the PDF from binary content
        pdf_document = fitz.open(stream=pdf_binary, filetype="pdf")
        num_pages = len(pdf_document)
        LOGGER.info("Opened PDF from binary content. found {} pages.".format(num_pages))

        text = ""
        for page_num in range(num_pages):
            text += "---- Page {} ----\n".format(page_num + 1)
            page = pdf_document.load_page(page_num)

            zoom = dpi / 72  # 72 is the default DPI of PDF
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat)
            image = Image.open(BytesIO(pix.tobytes()))
            text += pytesseract.image_to_string(image)

        pdf_document.close()
        LOGGER.info("text extracted from PDF successfully.")

    except fitz.FileNotFoundError:
        LOGGER.info("Error: PDF file not found.")

    return text