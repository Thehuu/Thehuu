#2 forms.py tạo form cho người dùng nhập thông tin từ giao diện
# Widget cho phép bạn thêm lớp CSS để đồng nhất giao diện, tăng tính thẩm mỹ và cải thiện trải nghiệm người dùng.

from django import forms
from .models import ReliefLocation, AccidentLocation


#tạo một ModelForm để người dùng có thể nhập thông tin và lưu vào cơ sở dữ liệu
#ModelForm là một lớp con của forms nhằm tạo ra các form
class ReliefLocationForm(forms.ModelForm):
    class Meta:
        model = ReliefLocation
        fields = ['name', 'mobile', 'latitude', 'longitude', 'description', 'image']

class AccidentLocationForm(forms.ModelForm):
    class Meta:
        model = AccidentLocation
        fields = ['name', 'mobile', 'latitude', 'longitude', 'description', 'image']