from django import forms
from cars.models import Carro

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = '__all__'

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco < 10000:
            self.add_error('preco', 'O preço não pode ser menor que R$ 10.000,00.')
        return preco