from django import forms
from .models import *

class MarketForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'