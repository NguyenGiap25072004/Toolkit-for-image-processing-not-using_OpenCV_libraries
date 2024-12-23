# Image Segmentation App

Ứng dụng này cung cấp các chức năng phân vùng ảnh (Image Segmentation) sử dụng các thuật toán **Thresholding** và **Canny Edge Detection**. Ứng dụng được viết bằng Python, sử dụng Tkinter cho giao diện và **không sử dụng** thư viện OpenCV cho các thuật toán xử lý ảnh chính.

## Cấu trúc thư mục

image_segmentation_app/
├── main.py # Ứng dụng chính cho Segmentation
├── image_processing/ # Module xử lý ảnh
│ ├── init.py
│ ├── utils.py # Các hàm tiện ích (đọc, ghi ảnh, chuyển đổi,...)
│ └── segmentation.py # Các hàm phân vùng ảnh
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
4.  Chọn phương pháp phân vùng ảnh (**Thresholding** hoặc **Canny Edge Detection**).
5.  **Thresholding:**
    - Nhập giá trị ngưỡng (**Threshold Value**) từ 0 đến 255.
    - Nhập giá trị lớn nhất (**Max Value**) (thường là 255).
    - Chọn phương pháp (`BINARY`, `BINARY_INV`, `TRUNC`, `TOZERO`, `TOZERO_INV`) từ combobox.
6.  **Canny Edge Detection:**
    - Nhập ngưỡng thấp (**Threshold 1**).
    - Nhập ngưỡng cao (**Threshold 2**).
7.  Nhấn nút **Process Image** để thực hiện phân vùng ảnh.
8.  Ảnh đã xử lý sẽ được hiển thị ở khung bên phải và tự động lưu vào đường dẫn đã chọn.

## Ghi chú

- Ứng dụng này **không sử dụng OpenCV** cho các thuật toán xử lý ảnh chính, giúp hiểu rõ hơn về bản chất của các thuật toán.
- Phiên bản hiện tại vẫn sử dụng **Pillow (PIL)** để đọc và ghi ảnh. Bạn có thể thay thế bằng các hàm tự viết để loại bỏ hoàn toàn phụ thuộc vào thư viện bên ngoài.
- Code cho phần `canny_edge_detection_no_opencv` chưa được triển khai. Đây là một công việc phức tạp đòi hỏi kiến thức sâu về xử lý ảnh và toán học.

## Tác giả

- Nguyễn Hữu Giáp

## Phiên bản

- 1.0
