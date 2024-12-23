# Image Compression App

Ứng dụng này cung cấp các chức năng nén ảnh (Image Compression) sử dụng hai phương pháp phổ biến:

- **JPEG (Joint Photographic Experts Group):** Nén mất dữ liệu, hiệu quả cho ảnh chụp tự nhiên.
- **PNG (Portable Network Graphics):** Nén không mất dữ liệu, phù hợp cho ảnh có các vùng màu đồng nhất, văn bản, hoặc các chi tiết sắc nét.

Ứng dụng được viết bằng Python, sử dụng Tkinter cho giao diện.

## Cấu trúc thư mục

image_compression_app/

├── main.py # Ứng dụng chính cho Image Compression

├── image_processing/ # Module xử lý ảnh

│ ├── init.py

│ ├── utils.py # Các hàm tiện ích (đọc, ghi ảnh, chuyển đổi,...)

│ └── compression.py # Các hàm nén ảnh

├── requirements.txt # Danh sách các thư viện cần thiết

└── README.md # Hướng dẫn sử dụng (file này)

## Yêu cầu

- Python 3.x
- Pillow
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

2.  Nhấn nút **Browse** ở phần **Input Image** để chọn ảnh cần nén.
3.  Nhấn nút **Browse** ở phần **Output Path** để chọn đường dẫn lưu ảnh đã nén.
4.  Chọn phương pháp nén (**JPEG** hoặc **PNG**).
5.  **JPEG:**
    - Nhập **Quality** (chất lượng nén) từ 0 đến 100 (mặc định là 75).
6.  **PNG:**
    - Nhập **Compression Level** (mức độ nén) từ 0 đến 9 (mặc định là 6).
7.  Nhấn nút **Process Image** để thực hiện nén ảnh.
8.  Ảnh đã nén sẽ được hiển thị ở khung bên phải và tự động lưu vào đường dẫn đã chọn.

## Ghi chú

- **JPEG:** Là phương pháp nén mất dữ liệu. Chất lượng ảnh sau khi nén sẽ giảm đi tùy thuộc vào giá trị **Quality** được chọn. Giá trị **Quality** càng thấp thì kích thước file càng nhỏ nhưng chất lượng ảnh càng kém.
- **PNG:** Là phương pháp nén không mất dữ liệu. Chất lượng ảnh được giữ nguyên sau khi nén.
- Phiên bản hiện tại đang sử dụng **Pillow (PIL)** để xử lý việc nén ảnh, do việc tự implement hoàn toàn JPEG và PNG là rất phức tạp.

## Tác giả

- Nguyễn Hữu Giáp

## Phiên bản

- 1.0
