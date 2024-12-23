# image_processing/enhancement.py
from .utils import read_image, save_image, image_to_list, list_to_image, calculate_histogram
from collections import defaultdict

def histogram_equalization_no_opencv(image_path, output_path):
    """
    Thực hiện cân bằng lược đồ xám (Histogram Equalization) không dùng OpenCV.

    Args:
        image_path (str): Đường dẫn đến ảnh.
        output_path (str): Đường dẫn lưu ảnh.

    Returns:
        None
    """
    img = read_image(image_path)
    if img is None:
        return

    img = img.convert("L")  # Convert to grayscale
    image_list = image_to_list(img)
    width, height = img.size

    histogram = calculate_histogram(image_list)
    total_pixels = width * height

    # Calculate cumulative distribution function (CDF)
    cdf = {}
    cumulative_sum = 0
    for value, count in sorted(histogram.items()):
        cumulative_sum += count
        cdf[value] = cumulative_sum

    # Equalize the image
    equalized_image = [[0] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            equalized_image[i][j] = round(255 * cdf[image_list[i][j]] / total_pixels)

    # Create a new image from the equalized pixel values
    equalized_img = list_to_image(equalized_image, width, height)

    # Save image
    save_image(equalized_img, output_path)

def clahe_no_opencv(image_path, output_path, clip_limit=2.0, tile_grid_size=(8, 8)):
    """
    Thực hiện CLAHE (Contrast Limited Adaptive Histogram Equalization) không dùng OpenCV.

    Args:
        image_path (str): Đường dẫn đến ảnh.
        output_path (str): Đường dẫn lưu ảnh.
        clip_limit (float): Ngưỡng giới hạn độ tương phản.
        tile_grid_size (tuple): Kích thước lưới ô.

    Returns:
        None
    """
    # Đọc ảnh và chuyển sang grayscale
    img = read_image(image_path)
    if img is None:
        return
    img = img.convert("L")
    image_list = image_to_list(img)
    width, height = img.size

    # Tính toán số ô theo chiều rộng và chiều cao
    tile_width = width // tile_grid_size[0]
    tile_height = height // tile_grid_size[1]

    # Xử lý phần dư
    remainder_width = width % tile_grid_size[0]
    remainder_height = height % tile_grid_size[1]

    # Tạo ảnh đầu ra
    clahe_image = [[0] * width for _ in range(height)]

    for i in range(tile_grid_size[1]):
        for j in range(tile_grid_size[0]):
            # Xác định vùng ô
            start_row, end_row = i * tile_height, (i + 1) * tile_height
            start_col, end_col = j * tile_width, (j + 1) * tile_width

            # Xử lý phần dư
            if i == tile_grid_size[1] - 1:
                end_row += remainder_height
            if j == tile_grid_size[0] - 1:
                end_col += remainder_width

            # Trích xuất ô từ ảnh
            tile = [row[start_col:end_col] for row in image_list[start_row:end_row]]

            # Tính histogram cho ô
            histogram = calculate_histogram(tile)

            # Giới hạn độ tương phản (clip histogram)
            # Tính toán ngưỡng clip_limit dựa trên số pixel trong ô
            max_count = clip_limit * (tile_width * tile_height) / len(histogram)
            excess = 0
            for k in histogram:
                if histogram[k] > max_count:
                    excess += histogram[k] - max_count
                    histogram[k] = max_count
            
            #Phân phối lại cho các pixel vượt ngưỡng
            redistribution = excess / len(histogram)
            for k in histogram:
                histogram[k] += redistribution

            # Tính CDF cho ô
            cdf = {}
            cumulative_sum = 0
            for value, count in sorted(histogram.items()):
                cumulative_sum += count
                cdf[value] = cumulative_sum

            # Cân bằng histogram cho ô
            tile_pixels = tile_width * tile_height
            for x in range(start_row, end_row):
                for y in range(start_col, end_col):
                    if x - start_row < len(tile) and y - start_col < len(tile[0]):
                        clahe_image[x][y] = round(255 * cdf[image_list[x][y]] / tile_pixels)

    # Chuyển đổi list of lists thành ảnh
    clahe_img = list_to_image(clahe_image, width, height)

    # Lưu ảnh
    save_image(clahe_img, output_path)