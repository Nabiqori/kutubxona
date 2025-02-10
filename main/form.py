from django import forms
from .models import *
class TalabaForm(forms.ModelForm):
    class Meta:
        model = Talaba
        fields = '__all__'
class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = '__all__'
class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
class KutubxonachiForm(forms.ModelForm):
    class Meta:
        model = Kutubxonachi
        fields = '__all__'