# forms.py
from django import forms
from .models import Zayavka


class ZayavkaForm(forms.ModelForm):
    class Meta:
        model = Zayavka
        fields = ['name', 'email', 'question', 'manager_id']

    manager_id = forms.IntegerField(widget=forms.HiddenInput())
