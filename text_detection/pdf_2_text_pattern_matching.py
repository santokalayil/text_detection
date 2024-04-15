
pdf_path = r"/Users/santokalayil/Developer/projects/text_detection/data/temp.pdf"
annotated_pdf_path = "/Users/santokalayil/Developer/projects/text_detection/data/annotated_pdf_file.pdf"


# # import fitz  # PyMuPDF
# # import re

# # # Function to perform text detection based on a pattern
# # def detect_text_with_pattern(text, pattern):
# #     detected_text = []
# #     for match in re.finditer(pattern, text):
# #         start_index = match.start()
# #         end_index = match.end()
# #         detected_text.append((start_index, end_index))
# #     return detected_text

# # # Open the PDF file
# # # pdf_path = "your_pdf_file.pdf"
# # pdf_document = fitz.open(pdf_path)

# # # Define the pattern for text detection
# # # pattern = r"\b\d{1,2}\.\d{1,2}\b"  # Example pattern for decimal numbers
# # pattern = r"\bhedg\w*\b"  # Pattern to match words containing 'hedg'

# # # Iterate through each page in the PDF
# # for page_num in range(len(pdf_document)):
# #     page = pdf_document.load_page(page_num)
    
# #     # Extract text from the page
# #     text = page.get_text()
    
# #     # Perform text detection on the extracted text
# #     detected_text_coordinates = detect_text_with_pattern(text, pattern)
    
# #     # Add bounding boxes as annotations to the page
# #     for start_index, end_index in detected_text_coordinates:
# #         # Calculate the position of the detected text
# #         start_pos = text.find(text[start_index:end_index])  # Find the position of the detected text in the entire page text
# #         end_pos = start_pos + len(text[start_index:end_index])
        
# #         # Get the bounding box of the detected text block
# #         text_block_bbox = page.search_for(text[start_index:end_index])[0]
        
# #         # Add some padding to the bounding box
# #         padding = 5
# #         bbox = fitz.Rect(text_block_bbox.x0 - padding,  # Adjust x-coordinate as needed
# #                          text_block_bbox.y0 - padding,  # Adjust y-coordinate as needed
# #                          text_block_bbox.x1 + padding,  # Adjust width as needed
# #                          text_block_bbox.y1 + padding)  # Adjust height as needed
# #         annot = page.add_rect_annot(bbox)
# #         annot.set_colors(stroke=(1, 0, 0), fill=(1, 0, 0, 0.2))  # Set stroke color to red and fill color to semi-transparent red

# # # Save the modified PDF with annotations
# # # annotated_pdf_path = "annotated_pdf_file.pdf"
# # pdf_document.save(annotated_pdf_path)
# # pdf_document.close()



# import fitz  # PyMuPDF
# import re

# # Function to perform text detection based on a pattern
# def detect_text_with_pattern(text, pattern):
#     detected_text = []
#     for match in re.finditer(pattern, text):
#         start_index = match.start()
#         end_index = match.end()
#         detected_text.append((start_index, end_index))
#     return detected_text

# # Open the PDF file
# # pdf_path = "your_pdf_file.pdf"
# pdf_document = fitz.open(pdf_path)

# # Define the pattern for text detection
# pattern = r"\bhedg\w*\b"  # Pattern to match words containing 'hedg'

# # Iterate through each page in the PDF
# for page_num in range(len(pdf_document)):
#     page = pdf_document.load_page(page_num)
    
#     # Extract text from the page
#     text = page.get_text()
    
#     # Perform text detection on the extracted text
#     detected_text_coordinates = detect_text_with_pattern(text, pattern)
    
#     # Print search results and page numbers
#     if detected_text_coordinates:
#         print(f"Search result found on page {page_num + 1}:")
#         for start_index, end_index in detected_text_coordinates:
#             print(f" - '{text[start_index:end_index]}'")
    
#     # Add bounding boxes as annotations to the page
#     for start_index, end_index in detected_text_coordinates:
#         # Calculate the position of the detected text
#         start_pos = text.find(text[start_index:end_index])  # Find the position of the detected text in the entire page text
#         end_pos = start_pos + len(text[start_index:end_index])
        
#         # Get the bounding box of the detected text block
#         text_block_bbox = page.search_for(text[start_index:end_index])[0]
        
#         # Add some padding to the bounding box
#         padding = 5
#         bbox = fitz.Rect(text_block_bbox.x0 - padding,  # Adjust x-coordinate as needed
#                          text_block_bbox.y0 - padding,  # Adjust y-coordinate as needed
#                          text_block_bbox.x1 + padding,  # Adjust width as needed
#                          text_block_bbox.y1 + padding)  # Adjust height as needed
#         annot = page.add_rect_annot(bbox)
#         annot.set_colors(stroke=(1, 0, 0), fill=(1, 0, 0, 0.2))  # Set stroke color to red and fill color to semi-transparent red

# # Save the modified PDF with annotations
# # annotated_pdf_path = "annotated_pdf_file.pdf"
# pdf_document.save(annotated_pdf_path)
# pdf_document.close()


import fitz  # PyMuPDF
import re

# Function to perform text detection based on a pattern
def detect_text_with_pattern(text, pattern):
    detected_text = []
    for match in re.finditer(pattern, text):
        start_index = match.start()
        end_index = match.end()
        detected_text.append((start_index, end_index))
    return detected_text

# Open the PDF file
# pdf_path = "your_pdf_file.pdf"
pdf_document = fitz.open(pdf_path)

# Define the pattern for text detection
pattern = r"\bhedg\w*\b"  # Pattern to match words containing 'hedg'

# List to store page numbers with annotations
pages_with_annotations = []

# Iterate through each page in the PDF
for page_num in range(len(pdf_document)):
    page = pdf_document.load_page(page_num)
    
    # Extract text from the page
    text = page.get_text()
    
    # Perform text detection on the extracted text
    detected_text_coordinates = detect_text_with_pattern(text, pattern)
    
    # Add bounding boxes as annotations to the page
    if detected_text_coordinates:
        # Store the page number if annotations are added
        pages_with_annotations.append(page_num)
        for start_index, end_index in detected_text_coordinates:
            # Calculate the position of the detected text
            start_pos = text.find(text[start_index:end_index])  # Find the position of the detected text in the entire page text
            end_pos = start_pos + len(text[start_index:end_index])
            
            # Get the bounding box of the detected text block
            text_block_bbox = page.search_for(text[start_index:end_index])[0]
            
            # Add some padding to the bounding box
            padding = 5
            bbox = fitz.Rect(text_block_bbox.x0 - padding,  # Adjust x-coordinate as needed
                             text_block_bbox.y0 - padding,  # Adjust y-coordinate as needed
                             text_block_bbox.x1 + padding,  # Adjust width as needed
                             text_block_bbox.y1 + padding)  # Adjust height as needed
            annot = page.add_rect_annot(bbox)
            annot.set_colors(stroke=(1, 0, 0), fill=(1, 0, 0, 0.2))  # Set stroke color to red and fill color to semi-transparent red

# Create a new PDF document for pages with annotations
new_pdf_document = fitz.open()
for page_num in pages_with_annotations:
    new_pdf_document.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

# Save the new PDF document with pages containing annotations
# annotated_pdf_path = "annotated_pdf_file_with_annotations.pdf"
new_pdf_document.save(annotated_pdf_path)
new_pdf_document.close()

# Close the original PDF document
pdf_document.close()
