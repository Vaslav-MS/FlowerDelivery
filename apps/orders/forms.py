from django import forms
from .models import Order

class OrderCheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_date', 'delivery_time', 'delivery_address']
        widgets = {
            'delivery_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'delivery_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'delivery_address': forms.TextInput(attrs={'class': 'form-control'}),
        }
