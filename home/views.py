from django.shortcuts import render
from .models import ReliefLocation, AccidentLocation
import requests
from django.conf import settings

def home(request):
    relief_locations = ReliefLocation.objects.all()
    accident_locations = AccidentLocation.objects.all()

    # Lấy dữ liệu dự báo thời tiết từ WeatherAPI
    weather_api_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        'key': settings.WEATHER_API_KEY,  # Lấy API key từ settings
        'q': 'Bac Kan, VN'
    }
    weather_response = requests.get(weather_api_url, params=params)
    weather_data = weather_response.json() if weather_response.status_code == 200 else None

    context = {
        'relief_locations': relief_locations,
        'accident_locations': accident_locations,
        'weather_data': weather_data
    }
    return render(request, 'pages/home.html', context)

def contact(request):
    return render(request, 'pages/contact.html')

def error_404(request, exception):
    return render(request, 'pages/error.html')

def error_500(request):
    return render(request, 'pages/error.html')

def register(request):
    return render(request, 'register.html')