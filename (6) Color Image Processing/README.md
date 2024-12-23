# Color Image Processing App

Ứng dụng này cung cấp các chức năng xử lý ảnh màu (Color Image Processing) bao gồm:

- **Convert to Grayscale:** Chuyển đổi ảnh màu sang ảnh đa mức xám.
- **Adjust Brightness:** Điều chỉnh độ sáng của ảnh.
- **Adjust Contrast:** Điều chỉnh độ tương phản của ảnh.
- **Adjust Saturation:** Điều chỉnh độ bão hòa màu của ảnh.

Ứng dụng được viết bằng Python, sử dụng Tkinter cho giao diện và **không sử dụng** thư viện `PIL.ImageEnhance` cho các thuật toán xử lý ảnh chính.

## Cấu trúc thư mục

color_image_processing_app/
├── main.py # Ứng dụng chính cho Color Image Processing
├── image_processing/ # Module xử lý ảnh
│ ├── init.py
│ ├── utils.py # Các hàm tiện ích (đọc, ghi ảnh, chuyển đổi,...)
│ └── color_processing.py # Các hàm xử lý ảnh màu
├── requirements.txt # Danh sách các thư viện cần thiết
└── README.md # Hướng dẫn sử dụng (file này)

## Yêu cầu

- Python 3.x
- Pillow (sẽ được thay thế bằng code tự viết sau này)
- ttkthemes

## Cài đặt

1.  Tạo môi trường ảo (virtual environment) - **đề xuất**:

    ```bash
    python3 -m venv venv
    ```

    Kích hoạt môi trường ảo:

    - **Windows:**

      ```bash
      venv\Scripts\activate
      ```

    - **macOS/Linux:**

      ```bash
      source venv/bin/activate
      ```

2.  Cài đặt các thư viện cần thiết:

    ```bash
    pip install -r requirements.txt
    ```

## Hướng dẫn sử dụng

1.  Chạy file `main.py`:

    ```bash
    python main.py
    ```

2.  Nhấn nút **Browse** ở phần **Input Image** để chọn ảnh cần xử lý.
3.  Nhấn nút **Browse** ở phần **Output Path** để chọn đường dẫn lưu ảnh.
4.  Nhấn nút chức năng tương ứng với thao tác bạn muốn thực hiện:
    - **Convert to Grayscale:** Chuyển ảnh sang ảnh grayscale.
    - **Adjust Brightness:** Điều chỉnh độ sáng (nhập factor trong hộp thoại).
    - **Adjust Contrast:** Điều chỉnh độ tương phản (nhập factor trong hộp thoại).
    - **Adjust Saturation:** Điều chỉnh độ bão hòa (nhập factor trong hộp thoại).
5.  Ảnh đã xử lý sẽ được hiển thị ở khung bên phải và tự động lưu vào đường dẫn đã chọn.

## Ghi chú

- Ứng dụng này **không sử dụng `PIL.ImageEnhance`** cho các thuật toán xử lý ảnh chính, giúp hiểu rõ hơn về bản chất của các thuật toán.
- Phiên bản hiện tại vẫn sử dụng **Pillow (PIL)** để đọc và ghi ảnh. Bạn có thể thay thế bằng các hàm tự viết để loại bỏ hoàn toàn phụ thuộc vào thư viện bên ngoài.
- Code cho các phần `adjust_brightness_no_pil`, `adjust_contrast_no_pil`, và `adjust_saturation_no_pil` cần được hoàn thiện.

## Tác giả

- Nguyễn Hữu Giáp

## Phiên bản

- 1.0
