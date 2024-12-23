# Image Enhancement App

Ứng dụng này cung cấp các chức năng tăng cường chất lượng ảnh (Image Enhancement) sử dụng các thuật toán **Histogram Equalization** và **Contrast Limited Adaptive Histogram Equalization (CLAHE)**. Ứng dụng được viết bằng Python và **không sử dụng** thư viện OpenCV hay bất kỳ thư viện xử lý ảnh nào khác (ngoại trừ Pillow/PIL để đọc và ghi ảnh ở phiên bản hiện tại).

## Cấu trúc thư mục

image_enhancement_app/
├── main_histogram_equalization.py  # Ứng dụng chính cho Histogram Equalization
├── main_clahe.py                 # Ứng dụng chính cho CLAHE
├── image_processing/             # Module xử lý ảnh (không dùng OpenCV)
│   ├── init.py
│   ├── utils.py                  # Các hàm tiện ích (đọc, ghi ảnh, chuyển đổi,...)
│   └── enhancement.py            # Các hàm tăng cường chất lượng ảnh
├── requirements.txt             # Danh sách các thư viện cần thiết (có thể chỉ có Pillow)
└── README.md                    # Hướng dẫn sử dụng (file này)

## Yêu cầu

*   Python 3.x
*   Pillow (sẽ được thay thế bằng code tự viết sau này)
*   ttkthemes

## Cài đặt

1.  Tạo môi trường ảo (virtual environment) - **đề xuất**:

    ```bash
    python3 -m venv venv
    ```

    Kích hoạt môi trường ảo:

    *   **Windows:**

        ```bash
        venv\Scripts\activate
        ```

    *   **macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

2.  Cài đặt các thư viện cần thiết:

    ```bash
    pip install -r requirements.txt
    ```

## Hướng dẫn sử dụng

### Histogram Equalization

1.  Chạy file `main_histogram_equalization.py`:

    ```bash
    python main_histogram_equalization.py
    ```

2.  Nhấn nút **Browse** ở phần **Input Image** để chọn ảnh cần xử lý.
3.  Nhấn nút **Browse** ở phần **Output Path** để chọn đường dẫn lưu ảnh.
4.  Nhấn nút **Process Image** để thực hiện cân bằng lược đồ xám.
5.  Ảnh đã xử lý sẽ được hiển thị ở khung bên phải và tự động lưu vào đường dẫn đã chọn.

### CLAHE

1.  Chạy file `main_clahe.py`:

    ```bash
    python main_clahe.py
    ```

2.  Nhấn nút **Browse** ở phần **Input Image** để chọn ảnh cần xử lý.
3.  Nhấn nút **Browse** ở phần **Output Path** để chọn đường dẫn lưu ảnh.
4.  Điều chỉnh các thông số **Clip Limit** và **Tile Grid Size** (nếu cần).
5.  Nhấn nút **Process Image** để thực hiện CLAHE.
6.  Ảnh đã xử lý sẽ được hiển thị ở khung bên phải và tự động lưu vào đường dẫn đã chọn.

## Ghi chú

*   Ứng dụng này **không sử dụng OpenCV** hay các thư viện xử lý ảnh khác cho các thuật toán chính, giúp hiểu rõ hơn về bản chất của các thuật toán.
*   Phiên bản hiện tại vẫn sử dụng **Pillow (PIL)** để đọc và ghi ảnh. Bạn có thể thay thế bằng các hàm tự viết để loại bỏ hoàn toàn phụ thuộc vào thư viện bên ngoài.
*   Code cho phần `clahe_no_opencv` chưa được tối ưu và còn một số hạn chế, bạn có thể tiếp tục hoàn thiện và phát triển thêm.

## Tác giả

*   Nguyễn Hữu Giáp

## Phiên bản

*   1.0