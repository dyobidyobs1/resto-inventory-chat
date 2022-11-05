from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StockForm(forms.ModelForm):
    class Meta:
        model = FoodInventory
        fields = "__all__"

class SalesForm(forms.ModelForm):
    class Meta:
        model = DailySales
        fields = "__all__"