# image_processing/segmentation.py
from .utils import read_image, save_image, image_to_list, list_to_image

def thresholding_no_opencv(image_path, output_path, threshold_value=127, max_value=255, method="BINARY"):
    """
    Phân ngưỡng ảnh (Thresholding) không dùng OpenCV.

    Args:
        image_path (str): Đường dẫn đến ảnh.
        output_path (str): Đường dẫn lưu ảnh.
        threshold_value (int): Ngưỡng phân loại. Mặc định là 127.
        max_value (int): Giá trị pixel lớn nhất sau khi phân ngưỡng. Mặc định là 255.
        method (str): Phương pháp phân ngưỡng. Mặc định là "BINARY".
                      Các phương pháp khác: "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV".

    Returns:
        None
    """
    img = read_image(image_path)
    if img is None:
        return

    img = img.convert("L")  # Convert to grayscale
    image_list = image_to_list(img)
    width, height = img.size

    # Apply thresholding
    thresholded_image = [[0] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if method == "BINARY":
                thresholded_image[i][j] = max_value if image_list[i][j] > threshold_value else 0
            elif method == "BINARY_INV":
                thresholded_image[i][j] = 0 if image_list[i][j] > threshold_value else max_value
            elif method == "TRUNC":
                thresholded_image[i][j] = threshold_value if image_list[i][j] > threshold_value else image_list[i][j]
            elif method == "TOZERO":
                thresholded_image[i][j] = image_list[i][j] if image_list[i][j] > threshold_value else 0
            elif method == "TOZERO_INV":
                thresholded_image[i][j] = 0 if image_list[i][j] > threshold_value else image_list[i][j]
            else:
                print("Error: Invalid thresholding method.")
                return

    # Create a new image from the thresholded pixel values
    thresholded_img = list_to_image(thresholded_image, width, height)

    # Save image
    save_image(thresholded_img, output_path)

def canny_edge_detection_no_opencv(image_path, output_path, threshold1=100, threshold2=200):
    """
    Phát hiện biên sử dụng thuật toán Canny không dùng OpenCV.

    Args:
        image_path (str): Đường dẫn đến ảnh.
        output_path (str): Đường dẫn lưu ảnh.
        threshold1 (int): Ngưỡng thấp cho hysteresis. Mặc định là 100.
        threshold2 (int): Ngưỡng cao cho hysteresis. Mặc định là 200.

    Returns:
        None
    """
    # TODO: Tự triển khai thuật toán Canny Edge Detection
    # Đây là một công việc phức tạp, đòi hỏi kiến thức sâu về xử lý ảnh và toán học.
    # Bạn cần tự nghiên cứu và triển khai dựa trên các tài liệu tham khảo.
    # Gợi ý:
    # 1. Đọc ảnh và chuyển sang grayscale (sử dụng các hàm trong utils.py).
    # 2. Khử nhiễu (ví dụ: sử dụng bộ lọc Gaussian tự viết).
    # 3. Tính toán gradient (độ lớn và hướng) bằng cách tự implement các toán tử Sobel, Prewitt, Roberts,...
    # 4. Thực hiện Non-maximum Suppression.
    # 5. Thực hiện Double Thresholding.
    # 6. Thực hiện Hysteresis Thresholding.
    # 7. Chuyển đổi ảnh về dạng phù hợp và lưu ảnh.

    print("Canny Edge Detection is not yet implemented.")
    pass