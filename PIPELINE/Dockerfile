# Sử dụng một image Python chính thống làm base image
FROM python:3.8-slim

# Thay đổi thư mục làm việc
WORKDIR /app

# Sao chép tất cả các file vào thư mục /app trong container
COPY . /app

# Cài đặt các dependency từ file requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mở cổng 80 để truy cập trang web
EXPOSE 8080

# Chạy ứng dụng Flask
CMD ["python", "app.py"]
