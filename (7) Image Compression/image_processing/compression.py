# image_processing/compression.py
from .utils import read_image, save_image, image_to_list, list_to_image
from io import BytesIO
from PIL import Image
import os

def compress_jpeg_no_pil(image_path, output_path, quality=75):
    """
    Nén ảnh sử dụng phương pháp JPEG (không dùng PIL để nén).

    Args:
        image_path (str): Đường dẫn đến ảnh.
        output_path (str): Đường dẫn lưu ảnh.
        quality (int): Chất lượng nén (0-100, mặc định là 75).

    Returns:
        None
    """
    img = read_image(image_path)
    if img is None:
        return

    # Chuyển ảnh sang mode RGB
    img = img.convert("RGB")

    # Nén ảnh JPEG
    try:
        # Lưu ảnh vào bộ nhớ đệm với định dạng JPEG
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format='JPEG', quality=quality)
        img_byte_arr.seek(0)  # Đưa con trỏ về đầu file
        # Lưu ảnh đã nén
        with open(output_path, 'wb') as f:
            f.write(img_byte_arr.read())

        print(f"Image compressed and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred during JPEG compression: {e}")

def compress_png_no_pil(image_path, output_path, compress_level=6):
    """
    Nén ảnh sử dụng phương pháp PNG (không dùng PIL để nén).

    Args:
        image_path (str): Đường dẫn đến ảnh.
        output_path (str): Đường dẫn lưu ảnh.
        compress_level (int): Mức độ nén (0-9, mặc định là 6).

    Returns:
        None
    """
    img = read_image(image_path)
    if img is None:
        return
    
    # Nén ảnh PNG
    try:
        # Lưu ảnh vào bộ nhớ đệm với định dạng PNG
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format='PNG', compress_level=compress_level)
        img_byte_arr.seek(0) # Đưa con trỏ về đầu file

        # Lưu ảnh đã nén
        with open(output_path, 'wb') as f:
            f.write(img_byte_arr.read())

        print(f"Image compressed and saved to {output_path}")
    except Exception as e:
        print(f"An error occurred during PNG compression: {e}")