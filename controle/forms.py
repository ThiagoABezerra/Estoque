from django import forms
from controle.models import Epi

class EpiFrom(forms.ModelForm):
    class Meta:
        model = Epi
        fields = ['name', 'ca', 'tamanho','estoque']
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'ca': forms.TextInput(attrs={'class': 'form-control'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control'}),            
            'tamanho': forms.TextInput(attrs={'class': 'form-control'}),
        }           
        


    
