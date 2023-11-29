import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny_operator(image_path, low_threshold, high_threshold):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image is valid
    if image is None:
        print("Unable to read the image.")
        return

    # Apply Canny Edge Detector
    edges = cv2.Canny(image, low_threshold, high_threshold)

    # Display the results
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap='gray')
    plt.title('Canny Edge Detector')

    plt.show()

# Image path
image_path = r'C:\Users\admin\Downloads\XLA\image\gojo.jpg'  # Change the path to your actual image

# Threshold values for Canny Edge Detector
low_threshold = 50
high_threshold = 150

# Apply Canny Edge Detector
canny_operator(image_path, low_threshold, high_threshold)
