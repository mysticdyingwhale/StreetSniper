import cv2
import pytesseract

# Load the image
image = cv2.imread('image_with_text.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use pytesseract to detect text boxes
boxes = pytesseract.image_to_boxes(gray)

# Loop through the detected text boxes and blur them
for box in boxes.splitlines():
    b = box.split(' ')
    x, y, x2, y2 = int(b[1]), int(b[2]), int(b[3]), int(b[4])

    # Extract the ROI (Region of Interest) containing the word
    word_roi = image[image.shape[0]-y2:image.shape[0]-y, x:x2]

    # Apply Gaussian blur to the ROI
    blurred_word = cv2.GaussianBlur(word_roi, (15, 15), 0)

    # Replace the original word with the blurred word
    image[image.shape[0]-y2:image.shape[0]-y, x:x2] = blurred_word

# Display or save the blurred image
cv2.imshow('Blurred Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


import requests

API_KEY = "YOUR_KEY"
location = "40.7128,-74.0060"  # NYC coordinates
url = f"https://maps.googleapis.com/maps/api/streetview?size=600x400&location={location}&key={API_KEY}"

response = requests.get(url)
with open("streetview.jpg", "wb") as f:
    f.write(response.content)

# console command (eval)?
# gsutil cp streetview.jpg gs://your-bucket/streetviews/

#CREATE TABLE streetview_images (
#    id INT AUTO_INCREMENT PRIMARY KEY,
#    location VARCHAR(255),
#    date_captured DATE,
#    gcs_url VARCHAR(255)
#);


# After uploading to GCS
gcs_url = "https://storage.googleapis.com/your-bucket/streetviews/streetview.jpg"

# Insert into MySQL
cursor.execute("""
    INSERT INTO streetview_images
    (location, date_captured, gcs_url)
    VALUES (%s, %s, %s)
""", (location, "2023-05-20", gcs_url))