# Image Restoration App

Ứng dụng này cung cấp các chức năng khôi phục ảnh (Image Restoration) sử dụng các thuật toán **Median Filter** và **Wiener Filter**. Ứng dụng được viết bằng Python, sử dụng Tkinter cho giao diện và **không sử dụng** thư viện OpenCV cho các thuật toán xử lý ảnh chính.

## Cấu trúc thư mục

image_restoration_app/

├── main_median_filter.py # Ứng dụng chính cho Median Filter

├── main_wiener_filter.py # Ứng dụng chính cho Wiener Filter

├── image_processing/ # Module xử lý ảnh

│ ├── init.py

│ ├── utils.py # Các hàm tiện ích (đọc, ghi ảnh, chuyển đổi,...)

│ └── restoration.py # Các hàm khôi phục ảnh

├── requirements.txt # Danh sách các thư viện cần thiết

└── README.

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

### Median Filter

1.  Chạy file `main_median_filter.py`:

    ```bash
    python main_median_filter.py
    ```

2.  Nhấn nút **Browse** ở phần **Input Image** để chọn ảnh cần xử lý.
3.  Nhấn nút **Browse** ở phần **Output Path** để chọn đường dẫn lưu ảnh.
4.  Điều chỉnh **Kernel Size** (kích thước kernel, phải là số lẻ).
5.  Nhấn nút **Process Image** để thực hiện lọc trung vị.
6.  Ảnh đã xử lý sẽ được hiển thị ở khung bên phải và tự động lưu vào đường dẫn đã chọn.

### Wiener Filter

1.  Chạy file `main_wiener_filter.py`:

    ```bash
    python main_wiener_filter.py
    ```

2.  Nhấn nút **Browse** ở phần **Input Image** để chọn ảnh cần xử lý.
3.  Nhấn nút **Browse** ở phần **Output Path** để chọn đường dẫn lưu ảnh.
4.  Nhấn nút **Process Image** để thực hiện lọc Wiener.
5.  Ảnh đã xử lý sẽ được hiển thị ở khung bên phải và tự động lưu vào đường dẫn đã chọn.

## Ghi chú

- Ứng dụng này **không sử dụng OpenCV** cho các thuật toán xử lý ảnh chính, giúp hiểu rõ hơn về bản chất của các thuật toán.
- Phiên bản hiện tại vẫn sử dụng **Pillow (PIL)** để đọc và ghi ảnh. Bạn có thể thay thế bằng các hàm tự viết để loại bỏ hoàn toàn phụ thuộc vào thư viện bên ngoài.
- Code cho phần `wiener_filter_no_opencv` chưa được triển khai. Đây là một công việc phức tạp đòi hỏi kiến thức sâu về xử lý tín hiệu và toán học.

## Tác giả

- \[Nguyễn Hữu Giáp]

## Phiên bản

- 1.0
