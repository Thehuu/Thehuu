# file định tuyến, xác định URL nào sẽ được xử lý bởi view nào

from django.urls import path, include #hàm từ module django.urls, ánh xạ URL
from . import views #tạo đối tượng view

# list URL app home (index, contact, register, login, logout)
urlpatterns = [
    path("", views.home, name='home'),  # Đặt tên để tham chiếu URL bằng {% url 'home' %}
    path("contact/", views.contact, name='contact'),
    path("404/", views.error_404, name='error_404'),
    path("500/", views.error_500, name='error_500'),
    path("accounts/", include('django.contrib.auth.urls')),
    path("register/", views.register, name='register'),  # Add this line for the register URL
]
