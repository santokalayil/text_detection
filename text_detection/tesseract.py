from pdf2image import convert_from_path

from paths import TESSERACT_PATH, DATA_DIR


def convert_pdf_to_images(pdf_file):
    return convert_from_path(pdf_file)


pdf_file = DATA_DIR / "AnnualReport2022-23_tata_motors.pdf"
images = convert_pdf_to_images(pdf_file)

import pytesseract

pytesseract.pytesseract.tesseract_cmd = str(TESSERACT_PATH)


def extract_text_from_images(images):
    text_list = []
    for image in images:
        text = pytesseract.image_to_string(image)
        text_list.append(text)
    return text_list


extracted_text = extract_text_from_images(images)

import pandas as pd
import re


def extract_table_data(text_list):
    tables = []
    for text in text_list:
        # Assuming each line of the table starts with a digit
        # (customize this regex based on your table format)
        lines = re.findall(r"^\d+.*", text, re.MULTILINE)
        # Split each line into columns
        table = [line.split() for line in lines]
        df = pd.DataFrame(table)
        tables.append(df)
    return tables


tables = extract_table_data(extracted_text)

pytesseract.image


image = images[157]
d = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
print(d)
