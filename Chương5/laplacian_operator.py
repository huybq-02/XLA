import cv2
import numpy as np
import matplotlib.pyplot as plt

def laplacian_operator(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image is valid
    if image is None:
        print("Unable to read the image.")
        return

    # Apply Laplacian Operator
    laplacian = cv2.Laplacian(image, cv2.CV_64F)

    # Display the results
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(laplacian, cmap='gray')
    plt.title('Laplacian Operator')

    plt.show()

# Image path
image_path = r'C:\Users\admin\Downloads\XLA\image\moon.jpg'  # Change the path to your actual image

# Apply Laplacian Operator
laplacian_operator(image_path)
