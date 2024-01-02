from django import forms
from brand_model.models import BrandModel


class BrandModelForm(forms.ModelForm):
    class Meta:
        model = BrandModel
        fields =['brand_name']