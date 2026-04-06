# 24120211_Lab1_API

## 1. Thông tin sinh viên

| Mục             | Thông tin                        |
| --------------- | -------------------------------- |
| Trường          | Đại học Khoa học Tự nhiên TP.HCM |
| Khoa            | Công nghệ Thông tin              |
| Môn học         | Tư duy Tính toán                 |
| Lớp             | 24CTT3                           |
| Họ và tên       | Lê Công Minh Nhựt                |
| Mã số sinh viên | 24120211                         |

## 2. Thông tin mô hình

| Mục                   | Thông tin                                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------------------- |
| Tên mô hình gốc       | Gemma 2 2B (Gemma-2-2b-it)                                                                              |
| Liên kết Hugging Face | [google/gemma-2-2b-it](https://huggingface.co/google/gemma-2-2b-it)                                     |
| Phiên bản tùy chỉnh   | `artyann-gemma` (Được cấu hình qua Ollama Modelfile để chuyên biệt hóa cho nhiệm vụ phân loại Spam/Ham) |

## 3. Mô tả chức năng hệ thống

Hệ thống là một API Web cung cấp dịch vụ phân loại văn bản/email tự động.

- **Đầu vào:** Một chuỗi văn bản hoặc nội dung email
- **Đầu ra:** Nhãn phân loại (`SPAM` cho thư rác/lừa đảo hoặc `HAM` cho thư thường) kèm theo mức độ tin cậy
- **Đặc điểm:** Tận dụng sức mạnh GPU T4 từ Google Colab để xử lý các mô hình ngôn ngữ lớn (LLM), giúp nhận diện ngữ cảnh tiếng Việt và tiếng Anh chính xác

## 4. Hướng dẫn cài đặt thư viện

Tại máy Local, bạn cần cài đặt các thư viện Python để chạy API Gateway:

```bash
pip install fastapi uvicorn requests pydantic
```

Lưu ý: Các thư viện nặng như torch hay transformers được chạy trực tiếp trên Colab để tiết kiệm tài nguyên máy cá nhân.

## 5. Hướng dẫn chạy chương trình

### Bước 1: Khởi động Model Server (Google Colab)

1. Mở file Notebook `[W2 - NOTEBOOK] API.ipynb` trên Colab
2. Chạy toàn bộ các cell để cài đặt Ollama, tạo mô hình tùy chỉnh và mở tunnel kết nối
3. Sao chép đường link Public hiện ra ở cell cuối cùng (ví dụ: `https://...a.free.pinggy.link`)

### Bước 2: Khởi động API Gateway (Local)

1. Mở file `main.py` ở máy tính cá nhân
2. Dán đường link vừa sao chép vào biến `COLAB_URL`
3. Chạy lệnh:

```bash
python main.py
```

## 6. Hướng dẫn gọi API và Ví dụ Request/Response

### Cách gọi API

Sử dụng công cụ Swagger UI tích hợp sẵn tại: `http://127.0.0.1:8000/docs`

### Ví dụ minh họa

**Request (POST):**

```json
{
  "text": "Chúc mừng! Bạn đã trúng thưởng 10 triệu đồng. Nhấn vào link để nhận ngay."
}
```

Response (JSON):

```json
{
  "label": "SPAM",
  "confidence": "High (Gemma 2 Engine)"
}
```
![](Lab1.mp4)
