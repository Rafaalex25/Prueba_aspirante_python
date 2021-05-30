from django import forms
from .models import *

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = [
            'centro_comercial',
            'distancia_comercial',
            'centro_comercial_visitado',
            
        ]
        labels = {  'centro_comercial':'Centro_comercial',
                    'distancia_comercial':'ruta',
                    'centro_comercial_visitado':'Centro_comercial',}