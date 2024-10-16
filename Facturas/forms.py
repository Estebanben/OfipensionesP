# Facturas/forms.py
from django import forms

class FacturaForm(forms.Form):
    start_date = forms.DateField(label='Fecha inicial', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='Fecha final', widget=forms.DateInput(attrs={'type': 'date'}))
    colegio_id = forms.IntegerField(label='ID del Colegio')
    
    