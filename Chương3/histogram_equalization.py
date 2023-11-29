import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(image_path):
    # Đọc ảnh từ đường dẫn
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Kiểm tra xem ảnh có tồn tại không
    if image is None:
        print("Không thể đọc được ảnh.")
        return

    # Thực hiện cân bằng histogram
    equalized_image = cv2.equalizeHist(image)

    # Hiển thị ảnh gốc và ảnh đã cân bằng histogram
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Ảnh Gốc')

    plt.subplot(1, 2, 2)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Cân Bằng Histogram')

    plt.show()

# Đường dẫn của ảnh
image_path = r'C:\Users\admin\Downloads\XLA\image\gojo.jpg'  # Thay đổi đường dẫn của ảnh thực tế

# Gọi hàm để thực hiện cân bằng histogram
histogram_equalization(image_path)
