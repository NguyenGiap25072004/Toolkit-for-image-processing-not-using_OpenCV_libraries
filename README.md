# Bộ Ứng Dụng Xử Lý Ảnh (Không Sử Dụng OpenCV)

Đây là bộ ứng dụng xử lý ảnh được viết bằng Python, **không sử dụng OpenCV** cho các thuật toán xử lý ảnh chính. Thay vào đó, các thuật toán được triển khai dựa trên lý thuyết và các công thức toán học, sử dụng Python thuần (có thể sử dụng `PIL/Pillow` cho việc đọc/ghi ảnh ở phiên bản hiện tại).

Bộ ứng dụng bao gồm:

1.  **Image Enhancement (Tăng cường chất lượng ảnh):**
    *   Histogram Equalization (Cân bằng lược đồ xám)
    *   CLAHE (Cân bằng lược đồ xám thích nghi có giới hạn độ tương phản)
2.  **Image Restoration (Khôi phục ảnh):**
    *   Median Filter (Lọc trung vị)
    *   Wiener Filter (Lọc Wiener) - *chưa triển khai*
3.  **Morphological Processing (Xử lý hình thái học):**
    *   Erosion (Phép co)
    *   Dilation (Phép giãn)
    *   Opening (Phép mở)
    *   Closing (Phép đóng)
4.  **Image Segmentation (Phân vùng ảnh):**
    *   Thresholding (Phân ngưỡng)
    *   Canny Edge Detection (Phát hiện biên Canny) - *chưa triển khai*
5.  **Object Recognition (Nhận dạng đối tượng):**
    *   Face Detection using Haar Cascade (Nhận diện khuôn mặt sử dụng Haar Cascade) - *chưa triển khai*
6.  **Color Image Processing (Xử lý ảnh màu):**
    *   Convert to Grayscale (Chuyển sang ảnh xám)
    *   Adjust Brightness (Điều chỉnh độ sáng)
    *   Adjust Contrast (Điều chỉnh độ tương phản)
    *   Adjust Saturation (Điều chỉnh độ bão hòa)
7.  **Image Compression (Nén ảnh):**
    *   JPEG Compression (Nén ảnh JPEG)
    *   PNG Compression (Nén ảnh PNG)

## Yêu cầu chung

*   Python 3.x
*   Pillow (sẽ được thay thế bằng code tự viết sau này)
*   ttkthemes

## Cài đặt

**Thực hiện các bước sau cho từng thư mục ứng dụng (ví dụ: `image_enhancement_app/`)**

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
    cd <tên_thư_mục_ứng_dụng>  # Ví dụ: cd image_enhancement_app
    pip install -r requirements.txt
    ```

## Hướng dẫn sử dụng

Mỗi ứng dụng có một file `README.md` riêng trong thư mục của nó. Vui lòng tham khảo file `README.md` trong từng thư mục để biết hướng dẫn sử dụng chi tiết cho từng ứng dụng.

## Ghi chú

*   Các ứng dụng này **không sử dụng OpenCV** cho các thuật toán xử lý ảnh chính (ngoại trừ `PIL/Pillow` cho việc đọc/ghi ảnh).
*   Một số chức năng nâng cao **chưa được triển khai** (Wiener Filter, Canny Edge Detection, Haar Cascade, ...). 
*   Phiên bản hiện tại vẫn sử dụng **Pillow (PIL)** để đọc và ghi ảnh. Bạn có thể thay thế bằng các hàm tự viết để loại bỏ hoàn toàn phụ thuộc vào thư viện bên ngoài.

## Tác giả

*   Nguyễn Hữu Giáp

## Phiên bản

*   1.0
