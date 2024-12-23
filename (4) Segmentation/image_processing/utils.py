# image_processing/utils.py
from PIL import Image
from collections import defaultdict

def read_image(image_path):
    """
    Đọc ảnh từ đường dẫn (sử dụng Pillow).

    Args:
        image_path (str): Đường dẫn đến ảnh.

    Returns:
        Image: Ảnh đọc từ file.
    """
    try:
        img = Image.open(image_path)
        return img
    except FileNotFoundError:
        print(f"Error: File not found at {image_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def save_image(image, output_path):
    """
    Lưu ảnh (sử dụng Pillow).

    Args:
        image (Image): Ảnh cần lưu.
        output_path (str): Đường dẫn lưu ảnh.

    Returns:
        None
    """
    try:
        image.save(output_path)
        print(f"Image saved to {output_path}")
    except Exception as e:
        print(f"An error occurred while saving: {e}")

def image_to_list(image):
    """
    Chuyển đổi ảnh sang dạng list of lists.

    Args:
        image (Image): Ảnh đầu vào.

    Returns:
        list: Ảnh dạng list of lists.
    """
    pixels = list(image.getdata())
    width, height = image.size
    return [pixels[i * width:(i + 1) * width] for i in range(height)]

def list_to_image(image_list, width, height, mode="L"):
    """
    Chuyển đổi list of lists sang ảnh.

    Args:
        image_list (list): Ảnh dạng list of lists.
        width (int): Chiều rộng ảnh.
        height (int): Chiều cao ảnh.
        mode (str): Chế độ màu ("L" cho grayscale, "RGB" cho màu).

    Returns:
        Image: Ảnh đầu ra.
    """
    new_img = Image.new(mode, (width, height))
    new_img.putdata([pixel for row in image_list for pixel in row])
    return new_img

def calculate_histogram(image):
    """
    Tính toán histogram của ảnh grayscale.

    Args:
        image (list): Ảnh grayscale (list of lists).

    Returns:
        dict: Histogram (key: mức xám, value: số pixel).
    """
    histogram = defaultdict(int)
    for row in image:
        for pixel in row:
            histogram[pixel] += 1
    return histogram