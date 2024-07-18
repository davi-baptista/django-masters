from django import forms
from cars.models import Car, Brand
    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value <= 0:
            self.add_error('value', 'Valor nulo ou negativo não são aceitos.')
        return value