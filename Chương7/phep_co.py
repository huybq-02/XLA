import cv2
import numpy as np
import matplotlib.pyplot as plt

def erosion_image(image_path, kernel_size=(3, 3)):
    # Read the grayscale image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image is valid
    if image is None:
        print("Unable to read the image.")
        return

    # Create a kernel for erosion
    kernel = np.ones(kernel_size, np.uint8)

    # Perform erosion
    eroded_image = cv2.erode(image, kernel, iterations=1)

    # Display the results
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(eroded_image, cmap='gray')
    plt.title('Eroded Image')

    plt.show()

# Example usage
image_path = r'C:\Users\admin\Downloads\XLA\image\gojo.jpg'    # Change the path to your actual image
erosion_image(image_path)
