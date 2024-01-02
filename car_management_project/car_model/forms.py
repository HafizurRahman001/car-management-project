from django import forms
from car_model.models import CarModel


class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        exclude = ['author']