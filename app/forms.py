from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from app.models import Vehicle

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class VehicleForm(forms.ModelForm):
    vehicle_model = forms.CharField(widget=forms.TextInput)
    vehicle_desc = forms.CharField(widget=forms.TextInput)
    class Meta:
        model = Vehicle
        fields = '__all__'


    def clean_vehicle_type(self):
        type = self.cleaned_data['vehicle_type']
        if type == '--select type--':
            raise forms.ValidationError('Select vehicle type')
        return type        
    
    def clean_vehicle_no(self):
        num = self.cleaned_data['vehicle_no']
        if not (num.isalnum()  and not num.isalpha() and not num.isdigit()):
            raise forms.ValidationError('Enter valid vehicle number')
        return num

