from django import forms
from controle.models import Epi

class EpiFrom(forms.ModelForm):
    class Meta:
        model = Epi
        fields = '__all__'
        
       
        


    
