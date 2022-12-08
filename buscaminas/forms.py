from django import forms
from django.core.exceptions import ValidationError


class FormTablero(forms.Form):
    filas = forms.IntegerField(label='Filas', max_value=20, min_value=1)
    columnas = forms.IntegerField(label='Columnas', max_value=20, min_value=1)
    minas = forms.IntegerField(label='Minas', max_value=20, min_value=1)

    def clean_minas(self):
        minas = self.cleaned_data['minas']
        filas = self.cleaned_data['filas']
        columnas = self.cleaned_data['columnas']
        if minas > (filas * columnas) / 2:
            raise ValidationError('Muchas minas')
        return minas
