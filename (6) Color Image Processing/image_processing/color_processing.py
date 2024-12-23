# image_processing/color_processing.py
from .utils import read_image, save_image, image_to_list, list_to_image
from PIL import Image, ImageEnhance

def convert_to_grayscale_no_pil(image_path, output_path):
    """
    Chuyển đổi ảnh sang ảnh grayscale (không dùng PIL.Image.convert).

    Args:
        image_path (str): Đường dẫn đến ảnh.
        output_path (str): Đường dẫn lưu ảnh.

    Returns:
        None
    """
    img = read_image(image_path)
    if img is None:
        return

    # Chuyển ảnh sang mode RGB
    img = img.convert("RGB")
    pixels = image_to_list(img)
    width, height = img.size

    gray_image = [[0] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            r, g, b = pixels[i][j]
            # Áp dụng công thức luminance
            gray_value = int(0.299 * r + 0.587 * g + 0.114 * b)
            gray_image[i][j] = gray_value

    # Create a new image from the grayscale pixel values
    gray_img = list_to_image(gray_image, width, height, mode="L")

    # Save image
    save_image(gray_img, output_path)

def adjust_brightness_no_pil(image_path, output_path, factor):
    """
    Điều chỉnh độ sáng của ảnh (không dùng PIL.ImageEnhance.Brightness).

    Args:
        image_path (str): Đường dẫn đến ảnh.
        output_path (str): Đường dẫn lưu ảnh.
        factor (float): Hệ số điều chỉnh độ sáng.

    Returns:
        None
    """
    img = read_image(image_path)
    if img is None:
        return
    
    # Chuyển ảnh sang mode RGB
    img = img.convert("RGB")
    pixels = image_to_list(img)
    width, height = img.size

    # Điều chỉnh độ sáng
    brightened_image = []
    for i in range(height):
        row = []
        for j in range(width):
            r, g, b = pixels[i][j]
            new_r = int(r * factor)
            new_g = int(g * factor)
            new_b = int(b * factor)

            # Giới hạn giá trị pixel trong khoảng 0-255
            new_r = max(0, min(new_r, 255))
            new_g = max(0, min(new_g, 255))
            new_b = max(0, min(new_b, 255))

            row.append((new_r, new_g, new_b))
        brightened_image.append(row)

    # Tạo ảnh mới từ các giá trị pixel đã được điều chỉnh
    brightened_img = list_to_image(brightened_image, width, height, mode="RGB")
    save_image(brightened_img, output_path)

def adjust_contrast_no_pil(image_path, output_path, factor):
    """
    Điều chỉnh độ tương phản của ảnh (không dùng PIL.ImageEnhance.Contrast).

    Args:
        image_path (str): Đường dẫn đến ảnh.
        output_path (str): Đường dẫn lưu ảnh.
        factor (float): Hệ số điều chỉnh độ tương phản.

    Returns:
        None
    """
    img = read_image(image_path)
    if img is None:
        return

    # Chuyển ảnh sang mode RGB
    img = img.convert("RGB")
    pixels = image_to_list(img)
    width, height = img.size

    # Tính toán giá trị trung bình của các kênh màu
    total_r, total_g, total_b = 0, 0, 0
    for i in range(height):
        for j in range(width):
            r, g, b = pixels[i][j]
            total_r += r
            total_g += g
            total_b += b
    avg_r = total_r / (width * height)
    avg_g = total_g / (width * height)
    avg_b = total_b / (width * height)

    # Điều chỉnh độ tương phản
    contrasted_image = []
    for i in range(height):
        row = []
        for j in range(width):
            r, g, b = pixels[i][j]
            new_r = int(avg_r + (r - avg_r) * factor)
            new_g = int(avg_g + (g - avg_g) * factor)
            new_b = int(avg_b + (b - avg_b) * factor)

            # Giới hạn giá trị pixel trong khoảng 0-255
            new_r = max(0, min(new_r, 255))
            new_g = max(0, min(new_g, 255))
            new_b = max(0, min(new_b, 255))

            row.append((new_r, new_g, new_b))
        contrasted_image.append(row)

    # Tạo ảnh mới từ các giá trị pixel đã được điều chỉnh
    contrasted_img = list_to_image(contrasted_image, width, height, mode="RGB")
    save_image(contrasted_img, output_path)

def adjust_saturation_no_pil(image_path, output_path, factor):
    """
    Điều chỉnh độ bão hòa của ảnh (không dùng PIL.ImageEnhance.Color).

    Args:
        image_path (str): Đường dẫn đến ảnh.
        output_path (str): Đường dẫn lưu ảnh.
        factor (float): Hệ số điều chỉnh độ bão hòa.

    Returns:
        None
    """
    img = read_image(image_path)
    if img is None:
        return

    # Chuyển ảnh sang mode RGB
    img = img.convert("RGB")
    pixels = image_to_list(img)
    width, height = img.size

    # Điều chỉnh độ bão hòa
    saturated_image = []
    for i in range(height):
        row = []
        for j in range(width):
            r, g, b = pixels[i][j]

            # Chuyển đổi RGB sang HSL
            max_rgb = max(r, g, b) / 255.0
            min_rgb = min(r, g, b) / 255.0
            delta = max_rgb - min_rgb

            l = (max_rgb + min_rgb) / 2.0

            if delta == 0:
                h = s = 0
            else:
                s = delta / (1 - abs(2 * l - 1))
                if max_rgb == r / 255.0:
                    h = 60 * (((g / 255.0) - (b / 255.0)) / delta % 6)
                elif max_rgb == g / 255.0:
                    h = 60 * (((b / 255.0) - (r / 255.0)) / delta + 2)
                else:
                    h = 60 * (((r / 255.0) - (g / 255.0)) / delta + 4)

            # Điều chỉnh độ bão hòa
            s *= factor

            # Giới hạn giá trị saturation trong khoảng 0-1
            s = max(0, min(s, 1))

            # Chuyển đổi HSL trở lại RGB
            c = (1 - abs(2 * l - 1)) * s
            x = c * (1 - abs((h / 60) % 2 - 1))
            m = l - c / 2

            if 0 <= h < 60:
                new_r, new_g, new_b = c, x, 0
            elif 60 <= h < 120:
                new_r, new_g, new_b = x, c, 0
            elif 120 <= h < 180:
                new_r, new_g, new_b = 0, c, x
            elif 180 <= h < 240:
                new_r, new_g, new_b = 0, x, c
            elif 240 <= h < 300:
                new_r, new_g, new_b = x, 0, c
            else:
                new_r, new_g, new_b = c, 0, x

            new_r = int((new_r + m) * 255)
            new_g = int((new_g + m) * 255)
            new_b = int((new_b + m) * 255)

            # Giới hạn giá trị pixel trong khoảng 0-255
            new_r = max(0, min(new_r, 255))
            new_g = max(0, min(new_g, 255))
            new_b = max(0, min(new_b, 255))

            row.append((new_r, new_g, new_b))
        saturated_image.append(row)

    # Tạo ảnh mới từ các giá trị pixel đã được điều chỉnh
    saturated_img = list_to_image(saturated_image, width, height, mode="RGB")
    save_image(saturated_img, output_path)