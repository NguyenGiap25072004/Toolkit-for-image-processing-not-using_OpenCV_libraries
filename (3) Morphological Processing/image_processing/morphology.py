# image_processing/morphology.py
from .utils import read_image, save_image, image_to_list, list_to_image

def erosion_no_opencv(image_path, output_path, kernel_size=3, iterations=1):
    """
    Thực hiện phép co (erosion) không dùng OpenCV.

    Args:
        image_path (str): Đường dẫn đến ảnh.
        output_path (str): Đường dẫn lưu ảnh.
        kernel_size (int): Kích thước kernel (lẻ). Mặc định là 3.
        iterations (int): Số lần lặp lại phép co. Mặc định là 1.

    Returns:
        None
    """
    img = read_image(image_path)
    if img is None:
        return

    img = img.convert("L")  # Convert to grayscale
    image_list = image_to_list(img)
    width, height = img.size

    # Tạo kernel
    kernel = [[1] * kernel_size for _ in range(kernel_size)]

    # Thực hiện phép co nhiều lần
    for _ in range(iterations):
        # Padding for the edges
        pad = kernel_size // 2
        padded_image = [[0] * (width + 2 * pad) for _ in range(height + 2 * pad)]
        for i in range(height):
            for j in range(width):
                padded_image[i + pad][j + pad] = image_list[i][j]

        # Apply erosion
        eroded_image = [[0] * width for _ in range(height)]
        for i in range(pad, height + pad):
            for j in range(pad, width + pad):
                min_val = 255  # Giá trị tối thiểu trong vùng lân cận
                for x in range(i - pad, i + pad + 1):
                    for y in range(j - pad, j + pad + 1):
                        if padded_image[x][y] < min_val:
                            min_val = padded_image[x][y]
                eroded_image[i - pad][j - pad] = min_val
        image_list = eroded_image # Cập nhật lại image_list cho lần lặp tiếp theo
    
    # Create a new image from the eroded pixel values
    eroded_img = list_to_image(image_list, width, height) # Đổi lại thành image_list

    # Save image
    save_image(eroded_img, output_path)

def dilation_no_opencv(image_path, output_path, kernel_size=3, iterations=1):
    """
    Thực hiện phép giãn (dilation) không dùng OpenCV.

    Args:
        image_path (str): Đường dẫn đến ảnh.
        output_path (str): Đường dẫn lưu ảnh.
        kernel_size (int): Kích thước kernel (lẻ). Mặc định là 3.
        iterations (int): Số lần lặp lại phép giãn. Mặc định là 1.

    Returns:
        None
    """
    img = read_image(image_path)
    if img is None:
        return

    img = img.convert("L")  # Convert to grayscale
    image_list = image_to_list(img)
    width, height = img.size
    
    # Tạo kernel
    kernel = [[1] * kernel_size for _ in range(kernel_size)]

    # Thực hiện phép giãn nhiều lần
    for _ in range(iterations):
        # Padding for the edges
        pad = kernel_size // 2
        padded_image = [[0] * (width + 2 * pad) for _ in range(height + 2 * pad)]
        for i in range(height):
            for j in range(width):
                padded_image[i + pad][j + pad] = image_list[i][j]

        # Apply dilation
        dilated_image = [[0] * width for _ in range(height)]
        for i in range(pad, height + pad):
            for j in range(pad, width + pad):
                max_val = 0  # Giá trị tối đa trong vùng lân cận
                for x in range(i - pad, i + pad + 1):
                    for y in range(j - pad, j + pad + 1):
                        if padded_image[x][y] > max_val:
                            max_val = padded_image[x][y]
                dilated_image[i - pad][j - pad] = max_val
        image_list = dilated_image # Cập nhật lại image_list cho lần lặp tiếp theo

    # Create a new image from the dilated pixel values
    dilated_img = list_to_image(image_list, width, height) # Đổi lại thành image_list

    # Save image
    save_image(dilated_img, output_path)

def opening_no_opencv(image_path, output_path, kernel_size=3):
    """
    Thực hiện phép mở (opening) không dùng OpenCV.

    Args:
        image_path (str): Đường dẫn đến ảnh.
        output_path (str): Đường dẫn lưu ảnh.
        kernel_size (int): Kích thước kernel (lẻ). Mặc định là 3.

    Returns:
        None
    """
    # Sử dụng các hàm erosion và dilation đã định nghĩa ở trên
    temp_path = "temp_opening.png"  # Đường dẫn tạm để lưu ảnh sau khi erosion
    erosion_no_opencv(image_path, temp_path, kernel_size, iterations=1)
    dilation_no_opencv(temp_path, output_path, kernel_size, iterations=1)

def closing_no_opencv(image_path, output_path, kernel_size=3):
    """
    Thực hiện phép đóng (closing) không dùng OpenCV.

    Args:
        image_path (str): Đường dẫn đến ảnh.
        output_path (str): Đường dẫn lưu ảnh.
        kernel_size (int): Kích thước kernel (lẻ). Mặc định là 3.

    Returns:
        None
    """
    # Sử dụng các hàm dilation và erosion đã định nghĩa ở trên
    temp_path = "temp_closing.png"  # Đường dẫn tạm để lưu ảnh sau khi dilation
    dilation_no_opencv(image_path, temp_path, kernel_size, iterations=1)
    erosion_no_opencv(temp_path, output_path, kernel_size, iterations=1)