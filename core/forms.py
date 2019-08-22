from django import forms


class AnoForm(forms.Form):
    ano = forms.IntegerField(label='Ano que deseja checar')