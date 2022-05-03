#Personalizacion de los campos
from django import forms
from .models import Prueba
#conectar campos con la vista


class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        #fields = ('__all__')
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )
        #personalizar formulario
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder' : 'Ingrese el texto',
                }
            )

        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            #pinta el error
            raise forms.ValidationError('Ingrese un numero mayor a 10')

        return cantidad

