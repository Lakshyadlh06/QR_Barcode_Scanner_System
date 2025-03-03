import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Read the first image
img1 = cv2.imread('barcode.jpeg')
# Read the second image
img2 = cv2.imread('qr.jpeg')

# Function to decode and display information from an image
def decode_image(img):
    for barcode in decode(img):
        # Decode the data
        myData = barcode.data.decode('utf-8')
        print(f"Decoded Data: {myData}")

        # Draw a rectangle around the barcode/QR code
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (0, 255, 0), 3)

        # Display the decoded text
        rect = barcode.rect
        cv2.putText(img, myData, (rect[0], rect[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Show the image with decoded information
    cv2.imshow('Decoded Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Decode each image
decode_image(img1)
decode_image(img2)
