#1 models.py
#Tạo bảng trong CSDL lưu trữ thông tin về các điểm cứu trợ
#db trong Django liên quan đến thao tác CSDL
#models định nghĩa các cấu trúc dữ liệu, các thuộc tính (fields), mối quan hệ
from django.db import models

class ReliefLocation(models.Model):
    name = models.CharField(max_length=100)  # Tên địa điểm cứu trợ
    mobile = models.CharField(max_length=15)  # Số điện thoại liên hệ
    latitude = models.DecimalField(max_digits=9, decimal_places=6)  # Vĩ độ
    longitude = models.DecimalField(max_digits=9, decimal_places=6)  # Kinh độ
    description = models.TextField(blank=True)  # Mô tả thêm về vị trí
    image = models.ImageField(upload_to='relief_images/', blank=True, null=True)  # Hình ảnh liên quan
    created_at = models.DateTimeField(auto_now_add=True)  # Thời gian tạo
    
    STATUS_CHOICES = [
        ('pending', 'Chờ duyệt'),
        ('approved', 'Duyệt'),
        ('rescued', 'Đã xong'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  # Trạng thái cứu trợ

    def __str__(self):
        return self.name

class AccidentLocation(models.Model):
    name = models.CharField(max_length=100)  # Tên địa điểm tai nạn
    mobile = models.CharField(max_length=15)  # Số điện thoại liên hệ
    latitude = models.DecimalField(max_digits=9, decimal_places=6)  # Vĩ độ
    longitude = models.DecimalField(max_digits=9, decimal_places=6)  # Kinh độ
    description = models.TextField(blank=True)  # Mô tả thêm về vị trí
    image = models.ImageField(upload_to='accident_images/', blank=True, null=True)  # Hình ảnh liên quan
    created_at = models.DateTimeField(auto_now_add=True)  # Thời gian tạo
    
    STATUS_CHOICES = [
        ('pending', 'Chờ duyệt'),
        ('approved', 'Duyệt'),
        ('resolved', 'Đã giải quyết'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  # Trạng thái tai nạn

    def __str__(self):
        return self.name

# Sau khi code hoàn thành cần chạy lệnh 

# python manage.py makemigrations 

# python manage.py migrate 

# Lệnh này sẽ áp dụng các thay đổi vào cơ sở dữ liệu, tạo các cột và bảng cần thiết