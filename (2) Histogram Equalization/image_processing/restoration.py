# image_processing/restoration.py
from .utils import read_image, save_image, image_to_list, list_to_image

def median_filter_no_opencv(image_path, output_path, kernel_size=3):
    """
    Áp dụng bộ lọc trung vị (Median Filter) không dùng OpenCV.

    Args:
        image_path (str): Đường dẫn đến ảnh.
        output_path (str): Đường dẫn lưu ảnh.
        kernel_size (int): Kích thước kernel (lẻ). Mặc định là 3.

    Returns:
        None
    """
    img = read_image(image_path)
    if img is None:
        return

    img = img.convert("L")  # Convert to grayscale
    pixels = list(img.getdata())
    width, height = img.size

    # Convert to list of lists
    image = [pixels[i * width:(i + 1) * width] for i in range(height)]

    # Padding for the edges
    pad = kernel_size // 2
    padded_image = [[0] * (width + 2 * pad) for _ in range(height + 2 * pad)]
    for i in range(height):
        for j in range(width):
            padded_image[i + pad][j + pad] = image[i][j]

    # Apply median filter
    filtered_image = [[0] * width for _ in range(height)]
    for i in range(pad, height + pad):
        for j in range(pad, width + pad):
            neighbors = []
            for x in range(i - pad, i + pad + 1):
                for y in range(j - pad, j + pad + 1):
                    neighbors.append(padded_image[x][y])
            neighbors.sort()
            filtered_image[i - pad][j - pad] = neighbors[len(neighbors) // 2]

    # Create a new image from the filtered pixel values
    filtered_img = list_to_image(filtered_image, width, height)

    # Save image
    save_image(filtered_img, output_path)

def wiener_filter_no_opencv(image_path, output_path):
    """
    Áp dụng bộ lọc Wiener (Wiener Filter) không dùng OpenCV.

    Args:
        image_path (str): Đường dẫn đến ảnh.
        output_path (str): Đường dẫn lưu ảnh.

    Returns:
        None
    """
    # TODO: Tự triển khai thuật toán Wiener Filter
    # Đây là một công việc phức tạp, đòi hỏi kiến thức sâu về xử lý tín hiệu và toán học.
    # Bạn cần tự nghiên cứu và triển khai dựa trên các tài liệu tham khảo.
    # Gợi ý:
    # 1. Đọc ảnh và chuyển sang grayscale (sử dụng các hàm trong utils.py).
    # 2. Thực hiện biến đổi Fourier (tự viết hàm hoặc sử dụng thư viện nếu được phép).
    # 3. Ước lượng các tham số của bộ lọc Wiener (H, S_ff, S_nn).
    # 4. Tính toán bộ lọc Wiener W trong miền tần số.
    # 5. Áp dụng bộ lọc Wiener lên ảnh đầu vào (trong miền tần số).
    # 6. Thực hiện biến đổi Fourier ngược để thu được ảnh đã lọc trong miền không gian.
    # 7. Chuyển đổi ảnh về dạng phù hợp và lưu ảnh.

    print("Wiener Filter is not yet implemented.")
    pass