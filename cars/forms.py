from django import forms
from cars.models import Carro

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = '__all__'