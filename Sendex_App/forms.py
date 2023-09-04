# sendex_app/forms.py
from django import forms
from .models import Shipment

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['sender_name', 'receiver_name', 'sender_phone', 'receiver_phone', 'sender_address', 'receiver_address', 'package_size']
