import cv2
import numpy as np
import matplotlib.pyplot as plt

def negative_transformation(image_path):
    # Đọc ảnh từ đường dẫn
    image = cv2.imread(image_path)

    # Kiểm tra xem ảnh có tồn tại không
    if image is None:
        print("Không thể đọc được ảnh.")
        return

    # Thực hiện biến đổi âm bản
    negative_image = 255 - image

    # Hiển thị ảnh gốc và ảnh đã biến đổi
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Ảnh Gốc')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(negative_image, cv2.COLOR_BGR2RGB))
    plt.title('Biến Đổi Âm Bản')

    plt.show()

# Đường dẫn của ảnh
image_path = r'C:\Users\admin\Downloads\XLA\image\gojo.jpg' # Thay đổi đường dẫn của ảnh thực tế

# Gọi hàm để thực hiện biến đổi âm bản
negative_transformation(image_path)
