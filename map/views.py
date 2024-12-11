#3 views.py functions điều khiển luồng xử lý dữ liệu giữa người dùng và DB 
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import ReliefLocation, AccidentLocation
from .forms import ReliefLocationForm, AccidentLocationForm

#render form cho người dùng nhập; render các điểm đã duyệt => map/map.html
def show_map(request):
    relief_form = ReliefLocationForm()
    accident_form = AccidentLocationForm()
    relief_locations = ReliefLocation.objects.filter(status='approved')
    accident_locations = AccidentLocation.objects.filter(status='approved')
    relief_data = [{'name': loc.name, 'mobile': loc.mobile, 'latitude': float(loc.latitude), 'longitude': float(loc.longitude), 'description': loc.description, 'image': loc.image.url if loc.image else ''} for loc in relief_locations]
    accident_data = [{'name': loc.name, 'mobile': loc.mobile, 'latitude': float(loc.latitude), 'longitude': float(loc.longitude), 'description': loc.description, 'image': loc.image.url if loc.image else ''} for loc in accident_locations]

    if request.method == 'POST':
        if 'relief_submit' in request.POST:
            relief_form = ReliefLocationForm(request.POST, request.FILES)
            if relief_form.is_valid():
                relief_form.save()
                return redirect('show_map')
        elif 'accident_submit' in request.POST:
            accident_form = AccidentLocationForm(request.POST, request.FILES)
            if accident_form.is_valid():
                accident_form.save()
                return redirect('show_map')

    return render(request, 'map/map.html', {'relief_form': relief_form, 'accident_form': accident_form, 'relief_locations': relief_data, 'accident_locations': accident_data})


#xử lý yêu cầu POST từ phía client.CHỖ NÀY CÓ LẼ CẦN NÚT BACK lại MAP
def save_location(request):
    if request.method == 'POST':
        form = ReliefPointForm(request.POST)
        if form.is_valid():
            location = form.save()
            return JsonResponse({'status': 'Gui_thanh_cong', 'location_id': location.id})
        else:
            return JsonResponse({'status': 'failed', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'failed'}, status=400)

