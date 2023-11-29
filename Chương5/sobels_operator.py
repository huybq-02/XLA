import cv2
import numpy as np
import matplotlib.pyplot as plt

def sobels_operator(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image is valid
    if image is None:
        print("Unable to read the image.")
        return

    # Apply Sobel Operator
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Compute the gradient magnitude
    gradient_magnitude = np.sqrt(np.square(sobel_x) + np.square(sobel_y))

    # Display the results
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 4, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 4, 2)
    plt.imshow(sobel_x, cmap='gray')
    plt.title('Sobel Operator (X-direction)')

    plt.subplot(1, 4, 3)
    plt.imshow(sobel_y, cmap='gray')
    plt.title('Sobel Operator (Y-direction)')

    plt.subplot(1, 4, 4)
    plt.imshow(gradient_magnitude, cmap='gray')
    plt.title('Gradient Magnitude')

    plt.show()

# Image path
image_path =  r'C:\Users\admin\Downloads\XLA\image\gojo.jpg' # Change the path to your actual image

# Apply Sobel Operator
sobels_operator(image_path)
