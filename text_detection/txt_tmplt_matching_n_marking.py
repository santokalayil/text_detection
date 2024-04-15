# import re
# import cv2
# import pytesseract
# from pytesseract import Output
# from pathlib import Path
# from matplotlib.pyplot import imshow, axis, show, figure

# filepath = Path(__file__).parent.parent / "data" / "page.png"

# img = cv2.imread(str(filepath))
# d = pytesseract.image_to_data(img, output_type=Output.DICT)
# keys = list(d.keys())

# # pattern = "^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$"
# pattern = r"[0-9]{1,2}\.[0-9]{1,2}"

# n_boxes = len(d["text"])
# for i in range(n_boxes):
#     if int(d["conf"][i]) > 60:
#         if re.match(pattern, d["text"][i]):
#             (x, y, w, h) = (d["left"][i], d["top"][i], d["width"][i], d["height"][i])
#             img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# # cv2.imshow("img", img)
# # cv2.waitKey(0)

# figure(figsize=(20, 30))
# img_rgb = img[::,:, ::-1]
# img_rgb = img[..., ::-1]
# imshow(img_rgb)
# axis('off')  # Turn off axis
# show()


# import re
# import cv2
# import pytesseract
# from pytesseract import Output
# from pathlib import Path
# from matplotlib.pyplot import imshow, axis, show, figure
# import numpy as np

# # Load the image
# filepath = Path(__file__).parent.parent / "data" / "page.png"
# img = cv2.imread(str(filepath))

# # Perform text detection
# d = pytesseract.image_to_data(img, output_type=Output.DICT)
# # pattern = r"[0-9]{1,2}\.[0-9]{1,2}"
# pattern = r"\b\d{1,2}\.\d{1,2}\b"

# # Define the size of the extra space
# extra_space = 200

# # Store detected text and their coordinates
# detected_text = []

# # Iterate over each text box
# for i in range(len(d["text"])):
#     if int(d["conf"][i]) > 60 and re.match(pattern, d["text"][i]):
#         (x, y, w, h) = (d["left"][i], d["top"][i], d["width"][i], d["height"][i])
#         # Draw bounding box on the original image
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
#         # Draw a line from the center of the bounding box to the extra space
#         center_x = x + w // 2
#         center_y = y + h // 2
#         cv2.line(img, (center_x, center_y), (img.shape[1] + extra_space, center_y), (255, 0, 0), 2)

#         # Extract the text and store it along with coordinates
#         detected_text.append((d["text"][i], img.shape[1] + 10, center_y))

# # Add extra space to the right side of the image
# img_with_extra_space = np.zeros((img.shape[0], img.shape[1] + extra_space, 3), dtype=np.uint8)
# img_with_extra_space[:, :img.shape[1]] = img

# # Convert image to RGB format for display in Matplotlib
# img_with_extra_space_rgb = cv2.cvtColor(img_with_extra_space, cv2.COLOR_BGR2RGB)



# # Print detected text in the extra space
# for text, x, y in detected_text:
#     cv2.putText(img_with_extra_space_rgb, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# # Display the modified image
# figure(figsize=(20, 30))
# imshow(img_with_extra_space_rgb)
# axis('off')
# show()




import re
import cv2
import pytesseract
from pytesseract import Output
from pathlib import Path
from matplotlib.pyplot import imshow, axis, show, figure
import numpy as np

# Load the image
filepath = Path(__file__).parent.parent / "data" / "page.png"
img = cv2.imread(str(filepath))

# Perform text detection
d = pytesseract.image_to_data(img, output_type=Output.DICT)
pattern = r"\b\d{1,2}\.\d{1,2}\b"

# Define the size of the extra space
extra_space = 200

# Store detected text and their coordinates
detected_text = []

# Iterate over each text box
for i in range(len(d["text"])):
    if int(d["conf"][i]) > 60 and re.match(pattern, d["text"][i]):
        (x, y, w, h) = (d["left"][i], d["top"][i], d["width"][i], d["height"][i])
        # Draw bounding box on the original image
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Draw a line slightly angled upwards from the center of the bounding box
        center_x = x + w // 2
        center_y = y + h // 2
        line_end_x = img.shape[1] + extra_space
        line_end_y = center_y - 200  # Adjust the vertical offset as needed
        cv2.line(img, (center_x, center_y), (line_end_x, line_end_y), (255, 0, 0), 2)

        # Extract the text and store it along with coordinates
        detected_text.append((d["text"][i], img.shape[1] + 10, center_y))

# Add extra space to the right side of the image
img_with_extra_space = np.zeros((img.shape[0], img.shape[1] + extra_space, 3), dtype=np.uint8)
img_with_extra_space[:, :img.shape[1]] = img

# Convert image to RGB format for display in Matplotlib
img_with_extra_space_rgb = cv2.cvtColor(img_with_extra_space, cv2.COLOR_BGR2RGB)

# Print detected text in the extra space
for text, x, y in detected_text:
    cv2.putText(img_with_extra_space_rgb, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Display the modified image
figure(figsize=(20, 30))
imshow(img_with_extra_space_rgb)
axis('off')
show()
